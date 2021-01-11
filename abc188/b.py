# -*- coding: UTF-8 -*-

# 入力
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# 内積
naiseki = 0
# 内積を計算
for i in range(N):
    naiseki += A[i] * B[i]
# 出力
if not naiseki:
    print('Yes')
else:
    print('No')