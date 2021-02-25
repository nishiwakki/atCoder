# -*- coding: UTF-8 -*-

import heapq

INF = 10 ** 12
# 入力
N, M = map(int, input().split())
A, B, C = [0]*M, [0]*M, [0]*M
for i in range(M):
    A[i], B[i], C[i] = map(int, input().split())
# 隣接リスト作成
adjb = [[] for _ in range(N+1)]
for i in range(M):
    adjb[A[i]].append((B[i], C[i]))
# 各街について
for sc in range(1, N+1):
    # 隣接リスト作成
    adj = [[] for _ in range(N+1)]
    for i in range(M):
        adj[A[i]].append((B[i], C[i]))
    # dijkstra
    dist = [INF] * (N+1)
    dist[sc] = 0
    que = [(dist[sc], sc)]
    heapq.heapify(que)
    reg = set()
    while que:
        t, c = heapq.heappop(que)
        if dist[c] < t:
            continue
        reg.add(c)
        while adj[c]:
            nc, nt = adj[c].pop()
            if nc in reg:
                continue
            if dist[nc] > dist[c] + nt:
                dist[nc] = dist[c] + nt
                heapq.heappush(que, (dist[nc], nc))
    # 街stから街stについて
    # INFで初期化
    ans = INF
    for c, adjc in enumerate(adjb):
        for nc, nt in adjc:
            if nc == sc:
                ans = min(ans, dist[c] + nt)
    # 出力
    if ans == INF:
        print(-1)
    else:
        print(ans)