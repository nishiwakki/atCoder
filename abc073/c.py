# -*- coding: UTF-8 -*-

# Aに出てくる数字とその個数をカウント
from collections import Counter

# 入力
N = int(input())
A = [int(input()) for _ in range(N)]
# 紙に書かれた数字の個数
ans = 0
for num, cnt in Counter(A).items():
    # 奇数なら紙に残るため
    if cnt % 2:
        ans += 1
# 出力
print(ans)