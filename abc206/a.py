# -*- coding: UTF-8 -*-

N = int(input())
if N*1.08//1 < 206:
    print('Yay!')
elif N*1.08//1 == 206:
    print('so-so')
else:
    print(':(')