# -*- coding: UTF-8 -*-

# 入力
A, B, C, D = map(int, input().split())
# 出力
if B < C or D < A:
    print('No')
else:
    print('Yes')