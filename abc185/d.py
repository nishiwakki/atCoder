# -*- coding: UTF-8 -*-

import math

# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
# 一度のハンコでOKな場合
if M == 0:
    print(1)
    exit()
# ハンコを使用する必要がない場合
elif M == N:
    print(0)
    exit()
# Aを昇順ソート
A.sort()
# 青マス間の最小マス数をチェック
# A[0] = 1でない場合
if A[0] - 1 > 0:
    min_dis = A[0] - 1
else:
    min_dis = N
for i in range(M-1):
    dis = A[i+1] - A[i] - 1
    # 青マスが隣接している場合は無視
    if not dis <= 0:
        # 最小値を更新
        min_dis = min(min_dis, dis)
# 答えのハンコ使用回数を保持
ans = 0
if not A[0] == 1:
    ans += math.ceil((A[0] - 1) / min_dis)
for i in range(M-1):
    ans += math.ceil((A[i+1] - A[i] - 1) / min_dis)
if not A[M-1] == N:
    ans += math.ceil((N - A[M-1]) / min_dis)
# 出力
print(ans)