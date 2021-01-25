# -*- coding: UTF-8 -*-

# 累積和ライブラリ
from itertools import accumulate

# 入力
N = int(input())
# 各行の累積和を計算
A1 = list(accumulate(map(int, input().split())))
A2 = list(accumulate(map(int, input().split())))
# 答えの最大値を保持
ans = 0
# 下方向移動するマスについて全探索
for i in range(N):
    if i == 0:
        ans = A1[i] + A2[N-1]
    else:
        ans = max(ans, A1[i] + A2[N-1] - A2[i-1])
# 出力
print(ans)