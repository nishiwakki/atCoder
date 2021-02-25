# -*- coding: UTF-8 -*-

# 入力
K, X = map(int, input().split())
# 出力
for i in range(X-K+1, X+K):
    print(i, end=' ')
# 改行入れる
print()