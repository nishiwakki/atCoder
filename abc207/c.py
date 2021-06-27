# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N = int(input())
t, l, r = [0]*N, [0]*N, [0]*N
for i in range(N):
    t[i], l[i], r[i] = map(int, input().split())
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        Li, Ri = l[i], r[i]
        Lj, Rj = l[j], r[j]
        if t[i] == 2:
            Ri -= 0.5
        elif t[i] == 3:
            Li += 0.5
        elif t[i] == 4:
            Ri -= 0.5
            Li += 0.5
        if t[j] == 2:
            Rj -= 0.5
        elif t[j] == 3:
            Lj += 0.5
        elif t[j] == 4:
            Rj -= 0.5
            Lj += 0.5
        if Ri < Lj:
            continue
        if Rj < Li:
            continue
        ans += 1
print(ans)