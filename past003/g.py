# -*- coding: UTF-8 -*-

from collections import deque

# INFINITY
INF = 2**10
# 入力
N, X, Y = map(int, input().split())
G = [[INF] * 405 for _ in range(405)]
# (-200, -200) -> (  2,   2)
# (   0,    0) -> (202, 202)
G[202][202] = 0
# 障害物の入力
for i in range(N):
    x, y = map(int, input().split())
    G[x+202][y+202] = -1
# キュー
q = deque([(202, 202)])
while q:
    x, y = q.popleft()
    # 外周に達したとき
    if x == 0 or x == 404 or y == 0 or y == 404:
        continue
    if G[x+1][y+1] == INF:
        G[x+1][y+1] = min(G[x+1][y+1], G[x][y]+1)
        q.append((x+1, y+1))
    if G[x][y+1] == INF:
        G[x][y+1] = min(G[x][y+1], G[x][y]+1)
        q.append((x, y+1))
    if G[x-1][y+1] == INF:
        G[x-1][y+1] = min(G[x-1][y+1], G[x][y]+1)
        q.append((x-1, y+1))
    if G[x+1][y] == INF:
        G[x+1][y] = min(G[x+1][y], G[x][y]+1)
        q.append((x+1, y))
    if G[x-1][y] == INF:
        G[x-1][y] = min(G[x-1][y], G[x][y]+1)
        q.append((x-1, y))
    if G[x][y-1] == INF:
        G[x][y-1] = min(G[x][y-1], G[x][y]+1)
        q.append((x, y-1))
# 出力
# 目標マス(X, Y)が更新されていないなら到達不可
if G[X+202][Y+202] == INF:
    print(-1)
else:
    print(G[X+202][Y+202])