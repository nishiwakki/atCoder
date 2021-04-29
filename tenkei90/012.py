# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

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

    def same(self, x, y):
        return self.find(x) == self.find(y)

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
G[x][y]: 上からx行目,左からy列目のマスについて
0:  白色マス
1~: 赤色マス(赤色マスが増えるたび+1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

H, W = map(int, input().split())
# indexErrorを避けるため少し大きめに用意
G = [[0] * (W+2) for _ in range(H+2)]
Q = int(input())
query = []
# ti = 1のクエリ数をカウント
cnt = 0
for q in range(Q):
    query.append(tuple(map(int, input().split())))
    if query[-1][0] == 1:
        cnt += 1
# 赤く塗ったマス分のunionFindを作成
uf = UnionFind(cnt)
num = 1
for q in query:
    # クエリ処理1
    if q[0] == 1:
        r, c = q[1], q[2]
        G[r][c] = num
        adj = set([G[r-1][c], G[r+1][c],
                   G[r][c-1], G[r][c+1]])
        for a in adj:
            if a:
                uf.union(num-1, a-1)
        num += 1
    # クエリ処理2
    else:
        ra, ca = q[1], q[2]
        rb, cb = q[3], q[4]
        a_num, b_num = G[ra][ca], G[rb][cb]
        if a_num == 0 or b_num == 0:
            print('No')
        else:
            if uf.same(a_num-1, b_num-1):
                print('Yes')
            else:
                print('No')