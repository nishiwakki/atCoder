# -*- coding: UTF-8 -*-

from collections import deque
import sys
input = sys.stdin.readline

INF = 10**6
N = int(input())
# 隣接リスト作成
# 最短距離を2回求めるため2つ用意
adj1 = [[] for _ in range(N+1)]
adj2 = [[] for _ in range(N+1)]
for i in range(N-1):
    A, B = map(int, input().split())
    adj1[A].append(B)
    adj1[B].append(A)
    adj2[A].append(B)
    adj2[B].append(A)
# dis_from_1[x]: 都市1 → 都市xまでの最短本数
dis_from_1 = [INF] * (N+1)
dis_from_1[0], dis_from_1[1] = 0, 0
# BFS1回目
# 起点は都市1
que = deque([1])
while que:
    now = que.popleft()
    while adj1[now]:
        next = adj1[now].pop()
        que.append(next)
        dis_from_1[next] = min(dis_from_1[next], 
                               dis_from_1[now]+1)
city = dis_from_1.index(max(dis_from_1))
# dis_from_2[x]: 都市city → 都市xまでの最短本数
dis_from_2 = [INF] * (N+1)
dis_from_2[0], dis_from_2[city] = 0, 0
# BFS2回目
# 起点は都市city
que = deque([city])
while que:
    now = que.popleft()
    while adj2[now]:
        next = adj2[now].pop()
        que.append(next)
        dis_from_2[next] = min(dis_from_2[next], 
                               dis_from_2[now]+1)
ans = max(dis_from_2) + 1
# 出力
print(ans)