# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline
from collections import deque

# 入力
H, W = map(int, input().split())
r, c = map(int, input().split())
s = [list(input().rstrip('\n')) for _ in range(H)]
# ゴールマスは当然'o'
s[r-1][c-1] = 'o'
# BFS
q = deque([(r-1, c-1)])
while q:
    x, y = q.popleft()
    # UP
    if x > 0:
        if s[x-1][y] == '.' or s[x-1][y] == 'v':
            s[x-1][y] = 'o'
            q.append((x-1, y))
    # DOWN
    if x < H-1:
        if s[x+1][y] == '.' or s[x+1][y] == '^':
            s[x+1][y] = 'o'
            q.append((x+1, y))
    # LEFT
    if y > 0:
        if s[x][y-1] == '.' or s[x][y-1] == '>':
            s[x][y-1] = 'o'
            q.append((x, y-1))
    # RIGHT
    if y < W-1:
        if s[x][y+1] == '.' or s[x][y+1] == '<':
            s[x][y+1] = 'o'
            q.append((x, y+1))
# 出力
for ss in s:
    for i in range(W):
        if not (ss[i] == 'o' or ss[i] == '#'):
            ss[i] = 'x'
    print(''.join(ss))