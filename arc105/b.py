# -*- coding: UTF-8 -*-

from math import gcd

# 入力
N = int(input())
a = list(map(int, input().split()))
# 答えを格納
ans = a[0]
# 最小公倍数(G.C.D)が答えとなる
for i in range(N-1):
    ans = min(ans, gcd(a[i], a[i+1]))
# 出力
print(ans)