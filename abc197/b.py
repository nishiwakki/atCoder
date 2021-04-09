# -*- coding: UTF-8 -*-

H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
# 0-origin
X, Y = X-1, Y-1
# (X, Y)自身をカウント
ans = 1
for i in range(X+1, H):
    if S[i][Y] == '.':
        ans += 1
    else:
        break
for i in range(X-1, -1, -1):
    if S[i][Y] == '.':
        ans += 1
    else:
        break
for i in range(Y+1, W):
    if S[X][i] == '.':
        ans += 1
    else:
        break
for i in range(Y-1, -1, -1):
    if S[X][i] == '.':
        ans += 1
    else:
        break
print(ans)