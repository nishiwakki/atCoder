# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline
from statistics import median

N = int(input())
X, Y = [0]*N, [0]*N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
midX, midY = int(median(X)), int(median(Y))
ans = sum([abs(X[i]-midX)+abs(Y[i]-midY) for i in range(N)])
print(ans)