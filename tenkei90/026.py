# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(adj, pr, st):
    if vstd[pr] == 1:
        vstd[st] = 2
    else:
        vstd[st] = 1
        ans.append(st)
    for next in adj[st]:
        if not vstd[next]:
            dfs(adj, st, next)

N = int(input())
adj = [[] for _ in range(N+1)]
for i in range(N-1):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)
vstd = [0] * (N+1)
vstd[0] = 2
ans = []
dfs(adj, 0, 1)
if len(ans) >= N//2:
    print(*ans[:N//2])
    exit()
vstd = [0] * (N+1)
vstd[0] = 1
ans = []
dfs(adj, 0, 1)
print(*ans[:N//2])