# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
sft = 0
for q in range(Q):
    T, x, y = map(int, input().split())
    x, y = x-1, y-1
    if T == 1:
        A[(x-sft)%N], A[(y-sft)%N] = \
            A[(y-sft)%N], A[(x-sft)%N]
    elif T == 2:
        sft += 1
    elif T == 3:
        print(A[(x-sft)%N])