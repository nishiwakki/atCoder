# -*- coding: UTF-8 -*-

# 入力
x, a, b = map(int, input().split())
# 出力
if abs(x-a) > abs(x-b):
    print('B')
else:
    print('A')