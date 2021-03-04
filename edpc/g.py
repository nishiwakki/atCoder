# -*- coding: UTF-8 -*-

from collections import deque
import sys
input = sys.stdin.readline

def topo_sort(N, adj):
    deg = [0] * N
    ret = [0] * N
    que = deque([])
    for u in adj:
        for v in u:
            deg[v] += 1
    for u in range(N):
        if not deg[u]:
            que.append(u)
    ret = []
    while que:
        u = que.popleft()
        ret.append(u)
        for v in adj[u]:
            deg[v] -= 1
            if not deg[v]:
                que.append(v)
    return ret[::-1]

# 入力
N, M = map(int, input().split())
x, y = [0] * M, [0] * M
for i in range(M):
    x[i], y[i] = map(int, input().split())
# 隣接リスト作成
adj = [[] for _ in range(N)]
for i in range(M):
    adj[x[i]-1].append(y[i]-1)
dp = [0] * N
# トポロジカルソート
ts = topo_sort(N, adj)
while ts:
    fm = ts.pop()
    while adj[fm]:
        to = adj[fm].pop()
        dp[to] = max(dp[to], dp[fm]+1)
# 出力
print(max(dp))