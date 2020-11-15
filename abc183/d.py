# -*- coding: UTF-8 -*-

# 入力
N, W = map(int, input().split())
S, T, P = [], [], []
for i in range(N):
    s, t, p = map(int, input().split())
    S.append(s)
    T.append(t)
    P.append(p)
# 各時刻ごとの使用リットルを管理
time = [0] * 200001
for i in range(N):
    time[S[i]] += P[i]
    # Tiちょうどは除くことに注意
    time[T[i]] -= P[i]
# TrueのときYes
ans = True
# その時刻での供給リットル
now = 0
for i in time:
    now += i
    # Wを超えているなら
    if now > W:
        ans = False
        break
# 出力
if ans:
    print('Yes')
else:
    print('No')