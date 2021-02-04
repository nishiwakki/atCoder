# -*- coding: UTF-8 -*-

# 順列全探索
from itertools import permutations
# 入力高速化
import sys
input = sys.stdin.readline

# 実質無限大
INF = 1_000_000_000

# 入力
N, M, R = map(int, input().split())
r = list(map(int, input().split()))
# 各町における最短距離
# WF[2][3]: 町2 → 町3
# 初期値は INF
WF = [[INF] * (N+1) for _ in range(N+1)]
# 町i → 町i は当然 0
for i in range(1, N+1):
    WF[i][i] = 0
# M本の道に関する入力
for _ in range(M):
    a, b, c = map(int, input().split())
    WF[a][b], WF[b][a] = c, c
# ワーシャルフロイド
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            WF[i][j] = min(WF[i][j], WF[i][k] + WF[k][j])
# 最短移動距離を INF で初期化
ans = INF
# 町の移動に関して順列全探索
for p in permutations(r, R):
    dist = 0
    for i in range(R-1):
        dist += WF[p[i]][p[i+1]]
    # 最短距離を更新
    ans = min(ans, dist)
# 出力
print(ans)