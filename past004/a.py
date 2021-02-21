# -*- coding: UTF-8 -*-

# 入力
A, B, C = map(int, input().split())
arr = sorted([A, B, C])
# arr[1] が 2番目に大きくなる
# 出力
if A == arr[1]:
    print('A')
elif B == arr[1]:
    print('B')
else:
    print('C')