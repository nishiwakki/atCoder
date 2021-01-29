# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

# 入力
H, W = map(int, input().split())
c = []
for i in range(10):
    c.append(list(map(int, input().split())))
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
# ワーシャルフロイド
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k]+c[k][j])
# 魔力の最小値
ans = 0
for a in A:
    for aa in a:
        if not aa == -1:
            ans += c[aa][1]
# 出力
print(ans)