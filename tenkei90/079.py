# -*- coding: UTF-8 -*-

H, W = map(int, input().split())
A = [list(map(int, input().split())) for h in range(H)]
B = [list(map(int, input().split())) for h in range(H)]
ans = 0
for h in range(H-1):
    for w in range(W-1):
        diff = B[h][w] - A[h][w]
        ans += abs(diff)
        A[h][w] += diff
        A[h+1][w] += diff
        A[h][w+1] += diff
        A[h+1][w+1] += diff
for h in range(H):
    if not A[h][W-1] == B[h][W-1]:
        ans = None
for w in range(W):
    if not A[H-1][w] == B[H-1][w]:
        ans = None
if ans is None:
    print('No')
else:
    print('Yes')
    print(ans)