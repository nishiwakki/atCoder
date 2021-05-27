# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = []
for i in range(N):
    A, B = map(int, input().split())
    s.append(B)
    s.append(A-B)
s.sort(reverse=True)
print(sum(s[0:K]))