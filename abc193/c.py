# -*- coding: UTF-8 -*-

# 入力
N = int(input())
# a^b で表せる数値をセットで管理
s = set()
for a in range(2, int(N**0.5)+1):
    i = a * a
    while i <= N:
        s.add(i)
        i *= a
# 出力
print(N - len(s))