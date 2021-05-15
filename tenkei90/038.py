# -*- coding: UTF-8 -*-

from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

A, B = map(int, input().split())
LCM = lcm(A, B)
if LCM > 10**18:
    print('Large')
else:
    print(LCM)