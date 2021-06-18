# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
inc = [A[i+1]-A[i] for i in range(N-1)]
ans = sum([abs(i) for i in inc])
for q in range(Q):
    L, R, V = map(int, input().split())
    if not L == 1:
        ans -= abs(inc[L-2])
        inc[L-2] += V
        ans += abs(inc[L-2])
    if not R == N:
        ans -= abs(inc[R-1])
        inc[R-1] += -V
        ans += abs(inc[R-1])
    print(ans)