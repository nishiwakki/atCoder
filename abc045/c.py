# -*- coding: UTF-8 -*-

from itertools import product

# [1, 2, 5] -> 125
def make_num(arr):
    val, dig = 0, 0
    while len(arr) > 0:
        num = arr.pop()
        val += 10 ** dig * num
        dig += 1
    return val

# 入力
S = input()
# 入力の長さ
l = len(S)
# 合計
ans = 0
# bit全探索
for pat in product(range(2), repeat=l-1):
    val = 0
    arr = [int(S[0])]
    for i in range(l-1):
        if pat[i]:
            val += make_num(arr)
            arr = []
        arr.append(int(S[i+1]))
    if len(arr) > 0:
        val += make_num(arr)
    ans += val
# 出力
print(ans)