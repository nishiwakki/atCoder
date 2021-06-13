# -*- coding: UTF-8 -*-

N = int(input())
A = list(map(int, input().split()))
n = [0] * (N+1)
for a in A:
    n[a] += 1
for i in range(1, N+1):
    if not n[i]:
        print('No')
        exit()
print('Yes')