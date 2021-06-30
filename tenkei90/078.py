# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
ans = 0
for i in range(N+1):
    cnt = 0
    for v in adj[i]:
        if v < i:
            cnt += 1
    if cnt == 1:
        ans += 1
print(ans)