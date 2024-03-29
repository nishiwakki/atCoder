# -*- coding: UTF-8 -*-

MOD = 10**9 + 7

N, L = map(int, input().split())
dp = [1] * (N+1)
for i in range(N+1):
    if i >= L:
        dp[i] = (dp[i-1]+dp[i-L]) % MOD
print(dp[N])