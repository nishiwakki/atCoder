# -*- coding: UTF-8 -*-

c = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
N = int(input())
ans = []
if N == 0:
    ans.append('0')
else:
    while N != 0:
        ans.append(c[N%36])
        N //= 36
print(''.join(reversed(ans)))