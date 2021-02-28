# -*- coding: UTF-8 -*-

# INFINITY
INF = 10 ** 9
# 入力
N, K = map(int, input().split())
h = list(map(int, input().split()))
# DP
dp = [INF] * N
dp[0] = 0
for i in range(N):
    for k in range(1, K+1):
        if i < N-k:
            dp[i+k] = min(dp[i+k], dp[i]+abs(h[i]-h[i+k]))
# 出力
print(dp[N-1])