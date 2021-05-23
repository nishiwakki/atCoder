# -*- coding: UTF-8 -*-

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
a, b, c = [0]*46, [0]*46, [0]*46
for aa in A:
    a[aa%46] += 1
for bb in B:
    b[bb%46] += 1
for cc in C:
    c[cc%46] += 1
ans = 0
for Ai in range(46):
    for Bi in range(46):
        for Ci in range(46):
            if (Ai+Bi+Ci) % 46 == 0:
                ans += a[Ai] * b[Bi] * c[Ci]
print(ans)