# -*- coding: UTF-8 -*-

from math import gcd

A, B, C = map(int, input().split())
D = gcd(gcd(A, B), C)
print(A//D + B//D + C//D - 3)