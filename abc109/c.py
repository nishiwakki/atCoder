# -*- coding: UTF-8 -*-

import math

# 入力
N, X = map(int, input().split())
x = list(map(int, input().split()))
# 出発点の座標を入れて
x.append(X)
# ソート
x.sort()
# 都市間の距離を取る
dis = []
for i in range(N):
    dis.append(x[i+1]-x[i])
ans = dis[0]
# 距離のG.C.Dがansとなる
for i in range(1, N):
    ans = math.gcd(ans, dis[i])
# 出力
print(ans)