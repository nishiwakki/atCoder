# -*- coding: UTF-8 -*-

# 入力
N = int(input())
K = int(input())
X = int(input())
Y = int(input())
# 出力
print(X * min(K, N) + Y * max(0, N-K))