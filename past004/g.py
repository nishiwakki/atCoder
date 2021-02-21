# -*- coding: UTF-8 -*-

from copy import deepcopy
from collections import deque

# 無限大を設定
INF = 1000
# 入力
N, M = map(int, input().split())
S = [[INF] * M for _ in range(N)]
ans = 0
for i in range(N):
    ss = input()
    for j in range(M):
        if ss[j] == '#':
            S[i][j] = -1
# 各マスについて
for n in range(N):
    for m in range(M):
        # INF は壁でないのでPASS
        if S[n][m] == INF:
            continue
        s = deepcopy(S)
        s[n][m] = 0
        # BFS
        que = deque([(n, m)])
        while que:
            y, x = que.popleft()
            if y > 0 and s[y-1][x] == INF:
                s[y-1][x] = s[y][x] + 1
                que.append((y-1, x))
            if y < N-1 and s[y+1][x] == INF:
                s[y+1][x] = s[y][x] + 1
                que.append((y+1, x))
            if x > 0 and s[y][x-1] == INF:
                s[y][x-1] = s[y][x] + 1
                que.append((y, x-1))
            if x < M-1 and s[y][x+1] == INF:
                s[y][x+1] = s[y][x] + 1
                que.append((y, x+1))
        # INFがあるとき未達マスがあることを示す
        flg = True
        for i in s:
            for j in i:
                if j == INF:
                    flg = False
        # 未達マスがないなら候補数+1
        if flg:
            ans += 1
# 出力
print(ans)