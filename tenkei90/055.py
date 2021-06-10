# -*- coding: UTF-8 -*-

from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for p in combinations(A, 5):
    if p[0]*p[1]%P*p[2]%P*p[3]%P*p[4]%P == Q:
        ans += 1
print(ans)