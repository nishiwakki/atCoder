# -*- coding: UTF-8 -*-

from math import factorial

# nCr: 二項係数(combination)
def comb(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

# 入力　
L = int(input())
# 出力
print(comb(L-1, 11))