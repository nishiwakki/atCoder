# -*- coding: UTF-8 -*-

# 入力
a, b = map(str, input().split())
# int型に変換して総和を求める
A = sum([int(i) for i in a])
B = sum([int(i) for i in b])
# 大きい方を出力
print(max(A, B))