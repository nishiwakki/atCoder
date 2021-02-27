# -*- coding: UTF-8 -*-

# 入力
N = int(input())
a = list(map(int, input().split()))
# 昇順ソート
a.sort()
# unpackで出力
print(*a)