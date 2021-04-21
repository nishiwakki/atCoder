# -*- coding: UTF-8 -*-

from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for q in range(Q):
    B = int(input())
    i = bisect_left(A, B)
    if i == 0:
        print(A[0]-B)
    elif i == N:
        print(B-A[N-1])
    else:
        print(min(B-A[i-1], A[i]-B))