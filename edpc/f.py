# -*- coding: UTF-8 -*-

# Longest Common Subsequence
def lcs(X, Y):
    dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
    for x in range(1, len(X)+1):
        for y in range(1, len(Y)+1):
            if X[x-1] == Y[y-1]:
                dp[x][y] = dp[x-1][y-1] + 1
            else:
                dp[x][y] = max(dp[x-1][y], dp[x][y-1])
    ret = ''
    x, y = len(X), len(Y)
    while dp[x][y]:
        if X[x-1] == Y[y-1]:
            ret += X[x-1]
            x -= 1
            y -= 1
        elif dp[x][y] == dp[x-1][y]:
            x -= 1
        else:
            y -= 1
    return ret[::-1]

# 入力
s = input()
t = input()
# 出力
print(lcs(s, t))