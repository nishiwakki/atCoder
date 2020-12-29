# -*- coding: UTF-8 -*-

# 入力
H, W = map(int, input().split())
# ブロックの個数を保持
A = [0] * H
# ブロックの個数の最小値を保持
m = 100
for i in range(H):
    A[i] = list(map(int, input().split()))
    # 最小値を更新
    m = min(m, min(A[i]))
# 取り除くブロックの個数
ans = 0
for a in A:
    for i in a:
        ans += i - m
# 出力
print(ans)