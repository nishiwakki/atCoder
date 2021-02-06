# -*- coding: UTF-8 -*-

# 入力
N = int(input())
S = input()
# 左から見たときの西を向いた人の累積和
E_from_E = [0] * N
for i in range(N):
    # 一番左の人について
    if i == 0:
        if S[0] == 'W':
            W_from_W[0] = 1
        continue
    if S[i] == 'W':
        W_from_W[i] = W_from_W[i-1] + 1
    else:
        W_from_W[i] = W_from_W[i-1]
# 右から見たときの東を向いた人の累積和
W_from_W = [0] * N
for i in range(N-1, -1, -1):
    # 一番右の人について
    if i == N-1:
        if S[N-1] == 'E':
            E_from_E[N-1] = 1
        continue
    if S[i] == 'E':
        E_from_E[i] = E_from_E[i+1] + 1
    else:
        E_from_E[i] = E_from_E[i+1]
# N人で初期化
ans = N
for i in range(N):
    # 一番左の人について
    if i == 0:
        cnt = E_from_E[i+1]
    # 一番右の人について
    elif i == N-1:
        cnt = W_from_W[i-1]
    else:
        cnt = E_from_E[i+1] + W_from_W[i-1]
    # 最小人数を更新
    ans = min(ans, cnt)
# 出力
print(ans)