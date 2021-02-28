# -*- coding: UTF-8 -*-

# INFINITY
INF = 10 ** 9
# 入力
N = int(input())
h = list(map(int, input().split()))
# DP
dp = [INF] * N
dp[0] = 0
for i in range(N):
    if i < N-1:
        dp[i+1] = min(dp[i+1], dp[i]+abs(h[i]-h[i+1]))
    if i < N-2:
        dp[i+2] = min(dp[i+2], dp[i]+abs(h[i]-h[i+2]))
# 出力
print(dp[N-1])