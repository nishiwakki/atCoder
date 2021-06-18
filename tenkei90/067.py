# -*- coding: UTF-8 -*-

def conv_8_to_9(x):
    x = x[::-1]
    val_10 = 0
    for i in range(len(x)):
        val_10 += 8 ** i * int(x[i])
    ret = []
    while val_10 > 0:
        if val_10%9 == 8:
            ret.append('5')
        else:
            ret.append(str(val_10%9))
        val_10 //= 9
    return ''.join(ret[::-1])

N, K = map(str, input().split())
if not N == '0':
    for k in range(int(K)):
        N = conv_8_to_9(N)
print(N)