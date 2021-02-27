# -*- coding: UTF-8 -*-

INF = 10 ** 10
# INFINITY で 初期化
ans = INF
# 入力
N = int(input())
for i in range(N):
    A, P, X = map(int, input().split())
    if X > A:
        # 最小金額を更新
        ans = min(ans, P)
# 出力
if ans == INF:
    print(-1)
else:
    print(ans)