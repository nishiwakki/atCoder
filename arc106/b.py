# -*- coding: UTF-8 -*-

# 入力高速化
import sys
input = sys.stdin.readline

# Union-Find
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
    
    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
            
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if not x == y:
            if self.parent[x] > self.parent[y]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

# 入力
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 頂点数NでUnionFind初期化
uf = UnionFind(N)
# M辺分を入力 & グループ併合
for i in range(M):
    c, d = map(int, input().split())
    # 0-originのため-1
    uf.union(c-1, d-1)
# 各頂点に対して
for i in range(N):
    # 1グループのa, bそれぞれの総和を格納
    aa, bb = 0, 0
    # 根までたどりつくまでのスタック
    stack = []
    next = uf.parent[i]
    prev = i
    while next >= 0:
        aa += a[prev]
        bb += b[prev]
        # 巡回済みは0を格納
        a[prev], b[prev] = 0, 0
        # スタックへ
        stack.append(next)
        prev = next
        next = uf.parent[next]
    # 根でないとき(根だとstackは空)
    if len(stack) > 0:
        # 最も直近にスタックにいれたのが根
        idx = stack.pop()
        a[idx] += aa
        b[idx] += bb
# 各頂点の総和をチェック
for i in range(N):
    if not a[i] == b[i]:
        print('No')
        exit()
print('Yes')