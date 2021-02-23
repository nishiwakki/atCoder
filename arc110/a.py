# -*- coding: UTF-8 -*-

from math import gcd

# 最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)

# 入力
N = int(input())
ans = 1
for i in range(2, N+1):
    ans = lcm(ans, i)
# 出力
print(ans + 1)