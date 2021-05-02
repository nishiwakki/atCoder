# -*- coding: UTF-8 -*-

from collections import deque
import sys
input = sys.stdin.readline

MAX = 2 * 10**5
N, M, K = map(int, input().split())
H = [0] + list(map(int, input().split()))
# 村 i から避難所まで最小 ans[i] 本の水路を要する
ans = [MAX] * (N+1)
C = list(map(int, input().split()))
# 避難所は ans[i] = 0
for c in C:
    ans[c] = 0
# 隣接リスト作成
adj = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, input().split())
    if H[A] < H[B]:
        adj[A].append(B)
    else:
        adj[B].append(A)
# BFS
q = deque(C)
while q:
    now = q.popleft()
    while adj[now]:
        next = adj[now].pop()
        if ans[now]+1 < ans[next]:
            ans[next] = ans[now] + 1
            q.append(next)
# 出力
for a in ans[1:]:
    # MAXのままなら辿り着けない
    if a == MAX:
        print(-1)
    else:
        print(a)