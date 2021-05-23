# -*- coding: UTF-8 -*-

from math import factorial

A, B, C = map(int, input().split())

def calc(x, y):
    return factorial(A+B-x-y) // factorial(A-x) // factorial(B-y)

ans = []
idx, a, b = 1, 1, 0
while not idx == C:
    # ループi回目に関して
    # 文字列i番目が b から始まる文字列は辞書順で bidx 番目
    bidx = idx + calc(a, b)
    if C < bidx:
        ans.append('a')
        a += 1
    else:
        ans.append('b')
        idx = bidx
        b += 1
a_cnt = ans.count('a')
b_cnt = ans.count('b')
if a_cnt < A:
    for i in range(A-a_cnt):
        ans.append('a')
if b_cnt < B:
    for i in range(B-b_cnt):
        ans.append('b')
print(''.join(ans))