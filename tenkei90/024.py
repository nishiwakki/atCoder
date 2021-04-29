# -*- coding: UTF-8 -*-

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
need = 0
for i in range(N):
    need += abs(A[i]-B[i])
if need > K:
    print('No')
else:
    if (K-need) % 2:
        print('No')
    else:
        print('Yes')