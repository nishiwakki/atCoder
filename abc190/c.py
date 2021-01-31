# -*- coding: UTF-8 -*-

from itertools import product

# 入力
N, M = map(int, input().split())
A, B = [0]*M, [0]*M
for i in range(M):
    A[i], B[i] = map(int, input().split())
K = int(input())
C, D = [0]*K, [0]*K
for i in range(K):
    C[i], D[i] = map(int, input().split())
# K人が 皿C(0) or 皿D(1) に
# ボールを置くかについて全探索
pats = product(range(2), repeat=K)
# 最大値を保持
ans = 0
for pat in pats:
    val = 0
    n = [0] * (N+1)
    # bit列に基づきボールを置く
    for i in range(K):
        if not pat[i]:
            n[C[i]] += 1
        else:
            n[D[i]] += 1
    # 全条件 M個 について
    for i in range(M):
        if n[A[i]] and n[B[i]]:
            val += 1
    # 最大値更新
    ans = max(ans, val)
# 出力
print(ans)