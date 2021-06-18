# -*- coding: UTF-8 -*-

MOD = 10**9 + 7

N, K = map(int, input().split())
if N == 1:
    print(K)
elif N == 2:
    if K == 1:
        print(0)
    else:
        print(K*(K-1)%MOD)
else:
    if K < 3:
        print(0)
    else:
        print(K*(K-1)*pow(K-2, N-2, MOD)%MOD)