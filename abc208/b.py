# -*- coding: UTF-8 -*-

from math import factorial

P = int(input())
S = [factorial(i) for i in range(10, 0, -1)]
ans = 0
for s in S:
    ans += P // s
    P %= s
print(ans)