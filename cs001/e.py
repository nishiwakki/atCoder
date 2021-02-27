# -*- coding: UTF-8 -*-

# 入力
N = int(input())
a = list(map(int, input().split()))
# 出力
# index(1)が早い
# 0-originのため +1
print(a.index(1)+1)