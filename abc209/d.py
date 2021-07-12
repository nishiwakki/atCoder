# -*- coding: UTF-8 -*-

from collections import deque
import sys
input = sys.stdin.readline

def BFS(vnum, sv, adj):
    dist = [-1] * (vnum+1)
    dist[sv] = 0
    que = deque([sv])
    while que:
        v = que.popleft()
        for x in adj[v]:
            if not dist[x] == -1:
                continue
            dist[x] = dist[v] + 1
            que.append(x)
    return dist[1:]

N, Q = map(int, input().split())
adj = [[] for _ in range(N+1)]
for n in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
dis = BFS(N, 1, adj)
for q in range(Q):
    c, d = map(int, input().split())
    if abs(dis[c-1]-dis[d-1]) % 2:
        print('Road')
    else:
        print('Town')