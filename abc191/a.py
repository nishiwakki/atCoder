# -*- coding: UTF-8 -*-

# 入力
V, T, S, D = map(int, input().split())
# 出力
if not T * V <= D <= S * V:
    print('Yes')
else:
    print('No')