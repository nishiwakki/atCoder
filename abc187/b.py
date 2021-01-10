# -*- coding: UTF-8 -*-

# 入力
N = int(input())
X, Y = [0] * N, [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
# 個数をカウント
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        # 直線の傾き
        slope = (Y[j]-Y[i]) / (X[j]-X[i])
        # 傾きが-1以上-1以下か?
        if -1 <= slope <= 1:
            ans += 1
# 出力
print(ans)