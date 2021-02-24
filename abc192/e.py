# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline
import heapq

INF = 10 ** 30
# 入力(1行目)
N, M, X, Y = map(int, input().split())
# 各都市までの最短時間を管理
ft = [INF] * (N+1)
# 都市Xから移動開始
ft[X] = 0
# 隣接リスト
adj = [[] for _ in range(N+1)]
# 入力(2行目以降)
for i in range(M):
    A, B, T, K = map(int, input().split())
    adj[A].append((B, T, K))
    adj[B].append((A, T, K))
# ダイクストラ法
pq = [(ft[X], X)]
heapq.heapify(pq)
reg = set()
while pq:
    t, c = heapq.heappop(pq)
    if ft[c] < t:
        continue
    reg.add(c)
    while adj[c]:
        nc, nt, k = adj[c].pop()
        # 既にncが最短パスに含まれる場合
        if nc in reg:
            continue
        # wt: Kの倍数になるまで待つ時間
        wt = 0
        if ft[c] % k:
            wt = k - (ft[c] % k)
        if ft[nc] > ft[c] + nt + wt:
            ft[nc] = ft[c] + nt + wt
            heapq.heappush(pq, (ft[nc], nc))
# INFなら都市Yに到達不可
if ft[Y] == INF:
    print(-1)
else:
    print(ft[Y])