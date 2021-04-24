# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip('\n'))
rev = False
pos = [i for i in range(2*N)]
Q = int(input())
for q in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if rev:
            if A < N:
                A += N
            else:
                A -= N
            if B < N:
                B += N
            else:
                B -= N
        pos[A-1], pos[B-1] = pos[B-1], pos[A-1]
    else:
        rev ^= True
ans = ''
if rev:
    for i in pos[N:]:
        ans += S[i]
    for i in pos[:N]:
        ans += S[i]
else:
    for i in pos:
        ans += S[i]
print(ans)