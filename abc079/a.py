# -*- coding: UTF-8 -*-

# 入力
N = input()
# 前3桁 or 後3桁 が全て同じか
# 出力
if N[0] == N[1] == N[2] or N[1] == N[2] == N[3]:
    print('Yes')
else:
    print('No')