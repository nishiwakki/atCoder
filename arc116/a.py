# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
N = 2**i + j(奇数)
i = 0: 正の偶数の約数を持たない
i = 1: 偶数・奇数が同じ個数になる
i ≥ 2: 正の奇数の約数の方が多くなる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if N % 4 == 0:
        print('Even')
    elif N % 2 == 0:
        print('Same')
    else:
        print('Odd')