# -*- coding: UTF-8 -*-

'''
任意の偶数 n について,
n xor (n+1) = 1
(最下位ビットが 0 か 1 の違い)
[(EX) n = 14]
14: 01110
15: 01111
A, Bを偶奇で場合分けして考える
'''

# 入力
A, B = map(int, input().split())
# A が 偶数
if A % 2 == 0:
    # B が 偶数
    if B % 2 == 0:
        if (B-A) % 4 == 0:
            print(0 ^ B)
        else:
            print(1 ^ B)
    # B が 奇数
    else:
        if (B-A+1) % 4 == 0:
            print(0)
        else:
            print(1)
# A が 奇数
else:
    # B が 偶数
    if B % 2 == 0:
        if (B-A-1) % 4 == 0:
            print(A ^ 0 ^ B)
        else:
            print(A ^ 1 ^ B)
    # B が 奇数
    else:
        if (B-A) % 4 == 0:
            print(0 ^ A)
        else:
            print(1 ^ A)