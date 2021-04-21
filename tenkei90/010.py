# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N = int(input())
cs1, cs2 = [0], [0]
for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        cs1.append(cs1[-1]+P)
        cs2.append(cs2[-1])
    else:
        cs1.append(cs1[-1])
        cs2.append(cs2[-1]+P)
Q = int(input())
for q in range(Q):
    L, R = map(int, input().split())
    print(cs1[R]-cs1[L-1], cs2[R]-cs2[L-1])