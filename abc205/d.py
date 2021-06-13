# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline
from bisect import bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
C = [A[i]-i for i in range(N)]
for q in range(Q):
    K = int(input())
    if C[N-1] <= K:
        print(A[N-1] + K - C[N-1] + 1)
    else:
        idx = bisect_right(C, K)
        if idx == 0:
            print(K)
        else:
            print(A[idx]+K-C[idx])