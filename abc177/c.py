# -*- coding: UTF-8 -*-

from itertools import accumulate

MOD = 10**9 + 7
# 入力
N = int(input())
A = list(map(int, input().split()))
# 累積和を計算
cumsumA = list(accumulate(A))
# 答えを格納
ans = 0
for i in range(N-1):
    # A[i+1] ~ A[N]までの和
    secsum = cumsumA[N-1] - cumsumA[i]
    ans += A[i] * secsum
    ans %= MOD
# 出力
print(ans)