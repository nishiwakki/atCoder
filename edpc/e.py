# -*- coding: UTF-8 -*-

# N, W入力
N, W = map(int, input().split())
# MAXV
MAXV = 10 ** 3 * N
# INFINITY
INF = 10 ** 12
# DPを0で初期化
dp = [[INF] * (MAXV+1) for _ in range(N+1)]
dp[0][0] = 0
# 各品物について
for i in range(1, N+1):
    # 品物入力
    w, v = map(int, input().split())
    # 各重さについて(貰うDP)
    for j in range(MAXV+1):
        if j-v >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v]+w)
        else:
            dp[i][j] = dp[i-1][j]
# 答えを求める
ans = INF
for v, w in enumerate(dp[N]):
    if w <= W:
        ans = v
# 出力
print(ans)