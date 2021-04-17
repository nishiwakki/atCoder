# -*- coding: UTF-8 -*-

MOD = 10**9 + 7
N, P = map(int, input().split())
print((P-1) * pow(P-2, N-1, MOD) % MOD)