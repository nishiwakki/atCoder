# -*- coding: UTF-8 -*-

# 入力
N, S, D = map(int, input().split())
# ダメージを与えられる呪文があるならTrue
ans = False
for i in range(N):
    # 入力
    X, Y = map(int, input().split())
    # X秒 < S秒 & 威力D < 威力Y
    # ならダメージを与えられる
    if X < S and D < Y:
        ans = True
# 出力
if ans:
    print('Yes')
else:
    print('No')