# -*- coding: UTF-8 -*-

N, A = map(int, input().split())
x = [0] + list(map(int, input().split()))
dp = [[[0]*(50*N+1) for i in range(N+1)] for j in range(N+1)]
dp[0][0][0] = 1
# 左からi番目までのカードの中から
for i in range(1, N+1):
    # j枚選んだときの(i枚以下)
    for j in range(i+1):
        # 整数の合計値について(50*j以下)
        for k in range(50*j+1):
            dp[i][j][k] = dp[i-1][j-1][k-x[i]] + dp[i-1][j][k]
ans = 0
for i in range(1, N+1):
    ans += dp[N][i][A*i]
print(ans)