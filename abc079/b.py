# -*- coding: UTF-8 -*-

# 入力
N = int(input())
# リュカ数
L = [0] * 87
# L0, L1を定義
L[0], L[1] = 2, 1
# L2 ~ L86 について
for i in range(2, 87):
    L[i] = L[i-2] + L[i-1]
# 出力
print(L[N])