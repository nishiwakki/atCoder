# -*- coding: UTF-8 -*-

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
Bi = [0] * (10**5 + 1)
for c in C:
    Bi[B[c-1]] += 1
ans = 0
for a in A:
    ans += Bi[a]
print(ans)