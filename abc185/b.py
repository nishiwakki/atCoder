# -*- coding: UTF-8 -*-

# 入力
N, M, T = map(int, input().split())
# バッテリー容量
n = N
# 最後の充電時刻
LT = 0
# M回シミュレーション
for i in range(M):
    A, B = map(int, input().split())
    # 最後の充電時刻から時刻Aまでのバッテリー消費量
    n -= A - LT
    # バッテリー残量が0以下になるならNo
    if n <= 0:
        print('No')
        exit()
    # バッテリー残量が容量の超過を防ぐ
    n = min(N, n + B - A)
    # 最後の充電時刻を更新
    LT = B
# 最後のカフェ滞在〜帰宅まで
if n - T + LT <= 0:
    print('No')
else:
    print('Yes')