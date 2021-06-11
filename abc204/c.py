# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# 隣接リスト作成
adj = [[] for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)

# BFS
# 都市svから移動可能な都市の数をreturn
def BFS(vnum, sv, adj):
    dist = [-1] * (vnum+1)
    dist[sv] = 0
    ret = 1
    que = deque([sv])
    while que:
        v = que.popleft()
        for x in adj[v]:
            if not dist[x] == -1:
                continue
            dist[x] = 0
            ret += 1
            que.append(x)
    return ret

# 組み合わせの答え
ans = 0
# 都市 1 ~ N 全ての街について
for frm in range(1, N+1):
    ans += BFS(N, frm, adj)
# 出力
print(ans)