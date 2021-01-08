# -*- coding: UTF-8 -*-

from itertools import product

# 入力
cookies = list(map(int, input().split()))
# 総和が等しいときTrue
ans = False
'''
# 全探索
for i in range(1 << 4):
    eaten, remain = 0, 0
    for j in range(4):
        if i >> j & 1:
            eaten += cookies[j]
        else:
            remain += cookies[j]
    if eaten == remain:
        ans = True
'''
for pat in product(range(2), repeat=4):
    eaten, remain = 0, 0
    for idx, bit in enumerate(pat):
        if bit:
            eaten += cookies[idx]
        else:
            remain += cookies[idx]
    if eaten == remain:
        ans = True
# 出力
if ans:
    print('Yes')
else:
    print('No')