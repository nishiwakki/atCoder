# -*- coding: UTF-8 -*-

MOD = 10 ** 9 + 7
# 入力
N = int(input())
a = list(map(str, input().split()))
# 出力(Pythonなら間に合う)
print(int(''.join(a)) % MOD)