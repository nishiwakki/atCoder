# -*- coding: UTF-8 -*-

n = int(input())
A = list(map(int, input().split()))
# [1] 1, -1, 1, ...
SUM1, SUM2 = 0, 0
# [2] -1, 1, -1, ...
ans1, ans2 = 0, 0
# [1]
for i in range(n):
    SUM1 += A[i]
    # SUM > 0
    if i % 2:
        inc = 0
        if SUM1 <= 0:
            inc = 1 - SUM1
        ans1 += inc
        SUM1 += inc
    # SUM < 0
    else:
        dec = 0
        if SUM1 >= 0:
            dec = SUM1 + 1
        ans1 += dec
        SUM1 -= dec
# [2]
for i in range(n):
    SUM2 += A[i]
    # SUM > 0
    if i % 2:
        dec = 0
        if SUM2 >= 0:
            dec = SUM2 + 1
        ans2 += dec
        SUM2 -= dec
    # SUM < 0
    else:
        inc = 0
        if SUM2 <= 0:
            inc = 1 - SUM2
        ans2 += inc
        SUM2 += inc
# output smaller one
print(min(ans1, ans2))