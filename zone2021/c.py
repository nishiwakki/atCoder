# -*- coding: UTF-8 -*-

# チームの総合力 x にできるか確認
def check(x):
    s = set()
    for i in range(N):
        t = [0] * 5
        if A[i] >= x:
            t[0] = 1
        if B[i] >= x:
            t[1] = 1
        if C[i] >= x:
            t[2] = 1
        if D[i] >= x:
            t[3] = 1
        if E[i] >= x:
            t[4] = 1
        s.add((tuple(t)))
    flg = False
    for i in s:
        for j in s:
            for k in s:
                tt = sum([i[0]|j[0]|k[0],
                          i[1]|j[1]|k[1],
                          i[2]|j[2]|k[2],
                          i[3]|j[3]|k[3],
                          i[4]|j[4]|k[4]])
                if tt == 5:
                    flg = True
    if flg:
        return True
    else:
        return False

# left  → True
# right → False
# に必ずなる決め打ち二分探索
def binary_search(lef, rig):
    while rig-lef > 1:
        mid = lef + (rig-lef) // 2
        if check(mid):
            lef = mid
        else:
            rig = mid
    return lef

import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D, E = [0]*N, [0]*N, [0]*N, [0]*N, [0]*N
for i in range(N):
    A[i], B[i], C[i], D[i], E[i] = map(int, input().split())
print(binary_search(1, 10**9+1))