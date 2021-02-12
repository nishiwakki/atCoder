# -*- coding: UTF-8 -*-

# 入力
N, K = map(int, input().split())
D = list(map(str, input().split()))
# N ~ 100000 まで全探索で必ずある
for n in range(N, 100001):
    ng = False
    for d in D:
        if d in str(n):
            ng = True
            break
    # 条件を満たすなら
    # 出力
    if not ng:
        print(n)
        exit()