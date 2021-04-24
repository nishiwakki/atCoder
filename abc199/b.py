# -*- coding: UTF-8 -*-

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_max, B_min = max(A), min(B)
if A_max > B_min:
    print(0)
else:
    print(B_min - A_max + 1)