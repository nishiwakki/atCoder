# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline
# distの初期化に使用
INF = 1_000_000_000
# 入力
N, M = map(int, input().split())
dist = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dist[i][i] = 0
a, b, c = [0] * M, [0] * M, [0] * M
for i in range(M):
    a[i], b[i], c[i] = map(int, input().split())
    dist[a[i]][b[i]], dist[b[i]][a[i]] = c[i], c[i]
# ワーシャルフロイド
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
# 最短経路に含まれない辺
ans = 0
# 各辺について,
# WFで更新された 頂点a - 頂点b の距離と
# 頂点a - 頂点b を結ぶ辺を比較し, 前者の方が長いなら,
# その経路は最短経路として使用されることはない
for i in range(M):
    if dist[a[i]][b[i]] < c[i]:
        ans += 1
# 出力
print(ans)