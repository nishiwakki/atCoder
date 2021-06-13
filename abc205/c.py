# -*- coding: UTF-8 -*-

A, B, C = map(int, input().split())
if C % 2:
    C = 1
else:
    C = 2
if pow(A, C) < pow(B, C):
    print('<')
elif pow(A, C) > pow(B, C):
    print('>')
else:
    print('=')