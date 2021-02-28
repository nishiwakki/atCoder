# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

# 入力
N = int(input())
a, b, c = [0]*(N+1), [0]*(N+1), [0]*(N+1)
for i in range(1, N+1):
    a[i], b[i], c[i] = map(int, input().split())
# dp[j][i]: i日目にjの活動を選んだ際の最大幸福度
# j=0:A, j=1:B, j=2:C
dp = [[0] * 3 for _ in range(N+1)]
dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0
for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][1]+a[i], dp[i-1][2]+a[i])
    dp[i][1] = max(dp[i-1][0]+b[i], dp[i-1][2]+b[i])
    dp[i][2] = max(dp[i-1][0]+c[i], dp[i-1][1]+c[i])
# 出力
print(max([dp[N][i] for i in range(3)]))