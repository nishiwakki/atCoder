# -*- coding: UTF-8 -*-

N, D, H = map(int, input().split())
ans = 0
for i in range(N):
    d, h = map(int, input().split())
    val = h - (H-h)/(D-d)*d
    ans = max(ans, val)
print(ans)