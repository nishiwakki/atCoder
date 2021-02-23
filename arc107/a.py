# -*- coding: UTF-8 -*-

MOD = 998_244_353
# 入力
A, B, C = map(int, input().split())
a = (1+A) * A // 2
b = (1+B) * B // 2
c = (1+C) * C // 2
# 出力
print(a * b * c % MOD)