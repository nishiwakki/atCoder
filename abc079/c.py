# -*- coding: UTF-8 -*-

from itertools import product

# 入力
N = input()
# 符号全パターンを作成
pats = product(['+', '-'], repeat=3)
# 各パターンについて
for pat in pats:
    val = int(N[0])
    for i in range(3):
        if pat[i] == '+':
            val += int(N[i+1])
        else:
            val -= int(N[i+1])
    # 左式 が 7 なら
    if val == 7:
        # 出力
        print(N[0] + pat[0] + N[1] + pat[1] + N[2] + pat[2] + N[3] + '=7')
        break