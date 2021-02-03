# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

# 入力
N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]
# 降順ソート
h.sort(reverse=True)
# K本の間隔ごとに h[max] - h[min] を計算
ans = h[0] - h[K-1]
for i in range(1, N-K+1):
    # 最小値を更新
    ans = min(ans, h[i]-h[i+K-1])
# 出力
print(ans)