# -*- coding: UTF-8 -*-

A = input()
B = input()
if len(A) > len(B):
    print('GREATER')
elif len(A) < len(B):
    print('LESS')
else:
    if A > B:
        print('GREATER')
    elif A < B:
        print('LESS')
    else:
        print('EQUAL')

'''
A = int(input())
B = int(input())
if A > B:
    print('GREATER')
elif A < B:
    print('LESS')
else:
    print('EQUAL')
'''