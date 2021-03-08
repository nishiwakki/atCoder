# -*- coding: UTF-8 -*-

# INFINITY
INF = 10 ** 12
# 入力
N, L = map(int, input().split())
X = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())
# ハードルがあるかどうか
is_Hurdle = [False] * (L+10)
for i in X:
    is_Hurdle[i] = True
# DP準備
# dp[i]: 座標iでの最短時間(秒数)
dp = [INF] * (L+10)
dp[0] = 0
# DP更新
for x in range(L):
    # act1
    if is_Hurdle[x+1]:
        dp[x+1] = min(dp[x+1], dp[x]+T1+T3)
    else:
        dp[x+1] = min(dp[x+1], dp[x]+T1)
    # act2
    if is_Hurdle[x+2]:
        dp[x+2] = min(dp[x+2], dp[x]+T1+T2+T3)
    else:
        dp[x+2] = min(dp[x+2], dp[x]+T1+T2)
    # act3
    if is_Hurdle[x+4]:
        dp[x+4] = min(dp[x+4], dp[x]+T1+3*T2+T3)
    else:
        dp[x+4] = min(dp[x+4], dp[x]+T1+3*T2)
# 答えを求める
# ジャンプ中にゴールする場合
ans = dp[L]
# Fin during act2
# before L-1
ans = min(ans, dp[L-1]+T1//2+T2//2)
# Fin during act3
# before L-2
ans = min(ans, dp[L-2]+T1//2+T2//2*3)
# before L-3
if L >= 3:
    ans = min(ans, dp[L-3]+T1//2+T2//2*5)
# 出力
print(ans)