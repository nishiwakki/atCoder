# -*- coding: UTF-8 -*-

class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.ret = 0
    
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
            self.ret += 1

    # the count of union
    def cnt(self):
        return self.ret

N = int(input())
A = list(map(int, input().split()))
uf = UnionFind(2 * 10**5 + 1)
for i in range(N//2):
    if not A[i] == A[N-i-1]:
        uf.union(A[i], A[N-i-1])
print(uf.cnt())