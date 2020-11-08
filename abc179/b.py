# -*- coding: UTF-8 -*-

# True時出力はYesとなる
ans = False
sameCnt = 0
# 入力
N = int(input())
for i in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        sameCnt += 1
    else:
        sameCnt = 0
    if sameCnt >= 3:
        ans = True
# 出力
if ans:
    print('Yes')
else:
    print('No')