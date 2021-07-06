# -*- coding: UTF-8 -*-

N, K = map(int, input().split())
a = list(map(int, input().split()))
aa = sorted(a)
if K % N:
    for A in a:
        if A <= aa[K%N-1]:
            print(K//N + 1)
        else:
            print(K//N)
else:
    for A in a:
        print(K//N)