# -*- coding: UTF-8 -*-

# 入力
N = int(input())
p = list(map(float, input().split()))
# DP準備 
# DP[i][j]: i枚目のコインまで投げた時, j枚が表の確率　
dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1
# DP
for j in range(1, N+1):
    frt, bak = p[j-1], 1-p[j-1]
    for i in range(j+1):
        # 0枚表: 1~j-1枚目が裏 * j枚目が裏
        if i == 0:
            dp[i][j] = dp[i][j-1] * bak
        # j枚表: 1~j-1枚目までj枚表 * j枚目が裏
        #     : 1~j-1枚目までj-1枚表 * j枚目が表
        else:
            dp[i][j] = dp[i-1][j-1]*frt + dp[i][j-1]*bak
# 答え
ans = 0
for i in range((N+1)//2, N+1):
    ans += dp[i][N]
# 出力
print(ans)