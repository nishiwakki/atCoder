# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
sum_H = []
for h in range(H):
    s = 0
    for w in range(W):
        s += A[h][w]
    sum_H.append(s)
sum_W = []
for w in range(W):
    s = 0
    for h in range(H):
        s += A[h][w]
    sum_W.append(s)
for h in range(H):
    pr = [] 
    for w in range(W):
        pr.append(sum_H[h] + sum_W[w] - A[h][w])
    print(*pr)