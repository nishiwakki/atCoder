# -*- coding: UTF-8 -*-

from math import gcd

# 最小公倍数
# [ex] lcm(4, 6) -> 12
def lcm(x, y):
    return x * y // gcd(x, y)

# 入力
N = int(input())
for i in range(N):
    T = int(input())
    if i == 0:
        ans = T
    else:
        ans = lcm(ans, T)
# 出力
print(ans)