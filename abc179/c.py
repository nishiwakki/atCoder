# -*- coding: UTF-8 -*-

#
# Python3.8.2だとTLE
# PyPy7.3.0ならAC
#

# 入力
N = int(input())
ans = 0
# 全探索
for A in range(1, 10**6):
    for B in range(1, 10**6):
        if A * B >= N:
            break
        ans += 1
# 出力
print(ans)