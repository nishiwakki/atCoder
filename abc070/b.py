# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
min(B,D) − max(A,C) 秒 : max(A,C) ≤ min(B,D)
                  0 秒 : max(A,C) > min(B,D)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# 入力
A, B, C, D = map(int, input().split())
# 出力
if max(A, C) <= min(B, D):
    print(min(B, D) - max(A, C))
else:
    print(0)