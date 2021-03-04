# -*- coding: UTF-8 -*-

MOD = 10 ** 9 + 7
# 入力
H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]
# DP準備
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
# DP
for h in range(H):
    for w in range(W):
        if a[h][w] == '#':
            continue
        if h == 0 and w == 0:
            continue
        elif h == 0:
            dp[h][w] = dp[h][w-1]
        elif w == 0:
            dp[h][w] = dp[h-1][w]
        else:
            dp[h][w] = (dp[h-1][w] + dp[h][w-1]) % MOD
# 出力
print(dp[H-1][W-1])