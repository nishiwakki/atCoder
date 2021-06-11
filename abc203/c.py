# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
frds = []
for i in range(N):
    a, b = map(int, input().split())
    frds.append((a, b))
# 太郎君に近い順にソート
frds.sort()
# 太郎君の行き着く村ans
ans = 0
# 最後に友達からお金を受け取った村
prev_a = 0
for a, b in frds:
    # 次の友達の村に辿り着けないとき
    if a - prev_a > K:
        ans += K
        K = 0
        break
    # 辿り着くとき
    else:
        ans += a - prev_a
        K -= a - prev_a
        K += b
        prev_a = a
ans += K
# 出力
print(ans)