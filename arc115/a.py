# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = [0] * 2
for n in range(N):
    cnt[input().count('1')%2] += 1
print(cnt[0] * cnt[1])