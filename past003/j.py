# -*- coding: UTF-8 -*-

import bisect

# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
# 答え
ans = [-1] * M
# ma[i]: i番目の子供が食べた最大美味しさ
ma = [0] * N
for i, a in enumerate(A):
    # 二分探索でサーチ
    who = bisect.bisect_right(ma, -a)
    if who >= N:
        continue
    ma[who] = -a
    ans[i] = who + 1
# 出力
for a in ans:
    print(a)