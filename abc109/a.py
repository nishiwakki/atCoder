# -*- coding: UTF-8 -*-

# 入力
A, B = map(int, input().split())
# 出力
if A * B % 2 == 0:
    print('No')
else:
    print('Yes')