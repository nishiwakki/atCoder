# -*- coding: UTF-8 -*-

N, K = map(int, input().split())
for i in range(K):
    if N % 200:
        N = int(str(N) + '200')
    else:
        N //= 200
print(N)