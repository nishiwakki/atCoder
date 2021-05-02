# -*- coding: UTF-8 -*-

from itertools import product

# 入力
N, M = map(int, input().split())
A, B, C = [], [], []
for i in range(M):
    a, b, c = map(int, input().split())
    A.append(a-1)
    B.append(b-1)
    C.append(c-1)
# 答えを保持
ans = 0
# 混ぜる薬品を全探索
for p in product(range(2), repeat=N):
    # resに含まれる薬品xは
    # 混ぜることで爆発するものをさす
    res = set([])
    for i in range(M):
        if p[A[i]] == 1 and p[B[i]] == 1 and p[C[i]] == 0:
            res.add(C[i])
        elif p[A[i]] == 1 and p[B[i]] == 0 and p[C[i]] == 1:
            res.add(B[i])
        elif p[A[i]] == 0 and p[B[i]] == 1 and p[C[i]] == 1:
            res.add(A[i])
    # 最大値を更新
    ans = max(ans, len(res))
# 出力
print(ans)