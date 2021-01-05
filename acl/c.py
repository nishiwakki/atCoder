# -*- coding: UTF-8 -*-

class UnionFind:
    def __init__(self, n):
        # 負のとき根
        self.n = n
        self.parent = [-1] * n
    
    # 要素xが属するグループの根を再帰サーチ
    def find(self, x):
        # xが負ならば根
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
            
    # 要素xが属するグループ と 要素yが属するグループを併合する
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        # 根が共通でないとき
        if not x == y:
            # 根同士ならサイズをチェック
            if self.parent[x] > self.parent[y]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

    # 要素xが属するグループのサイズ(要素数)を返す
    def size(self, x):
        return -self.parent[self.find(x)]

    # 要素x, yが同じグループに属するかどうかを返す
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 根の要素が何かを返す
    # [Ex] [-4, -1, 0, 0, -1, 3]
    # -> [0, 1, 4]
    def roots(self):
        root_list = []
        for idx, siz in enumerate(self.parent):
            if siz < 0:
                root_list.append(idx)
        return root_list
    
    # 集合数を返す
    def count(self):
        cnt = 0
        for siz in self.parent:
            if siz < 0:
                cnt += 1
        return cnt

# 入力
N, M = map(int, input().split())
# 要素数Nのunion-find構造を作成
uf = UnionFind(N)
# M個の道路について
for i in range(M):
    A, B = map(int, input().split())
    uf.union(A-1, B-1)
# グループの数-1 が出力する答え
print(uf.count() - 1)