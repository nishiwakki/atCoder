# -*- coding: UTF-8 -*-

N = int(input())
b_max = 0
for i in range(61):
    if 2**i < N:
        b_max = i
ans = 10**19
for b in range(b_max+1):
    a = N // 2 ** b
    c = N - a * 2 ** b
    ans = min(ans, a+b+c)
print(ans)