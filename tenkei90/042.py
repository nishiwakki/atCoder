# -*- coding: UTF-8 -*-

MOD = 10**9 + 7

K = int(input())
if K % 9:
    print(0)
else:
    # dp[各桁の数字の和] = 通り
    dp = [0] * (K+1)
    dp[0] = 1
    for i in range(1, K+1):
        for j in range(1, min(i, 9)+1):
            dp[i] = (dp[i] + dp[i-j]) % MOD
        #print(i, dp)
    print(dp[K])