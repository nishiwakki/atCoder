# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N = int(input())
s = set([])
for i in range(N):
    S = input()
    if not S in s:
        print(i+1)
        s.add(S)