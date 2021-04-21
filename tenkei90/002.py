# -*- coding: UTF-8 -*-

from itertools import product

N = int(input())
for p in product(['(', ')'], repeat=N):
    a = 0
    flg = True
    for pp in p:
        if pp == '(':
            a += 1
        else:
            a -= 1
        if a < 0:
            flg = False
            break
    if flg and a == 0:
        print(''.join(p))