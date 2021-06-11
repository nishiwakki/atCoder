# -*- coding: UTF-8 -*-

# 部分和問題
# 動的計画法(DP) で解くのが定番

N = int(input())
T = list(map(int, input().split()))
MAX = sum(T) + 1
# dp[i][j]
# 料理i までいくつかの料理を作るとき
# 時間t で作ることができるなら True
dp = [[False] * MAX for _ in range(N+1)]
dp[0][0] = True
for i in range(1, N+1):
    for j in range(MAX):
        # 料理i を作らない
        dp[i][j] = dp[i-1][j]
        # 料理i を作る
        if j-T[i-1] >= 0:
            if dp[i-1][j-T[i-1]]:
                dp[i][j] = True
# 最短でも (全料理の時間和//2) より長くなる
for t in range(MAX//2, MAX):
    if dp[N][t]:
        print(t)
        break