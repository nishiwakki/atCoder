# -*- coding: UTF-8 -*-

# (R, X, Y) = (1, 10**5, 10**5)
# 141422 より ループ回数 150000

R, X, Y = map(int, input().split())
if R**2 > X**2 + Y**2:
    print(2)
else:
    for i in range(150000):
        if (R*i)**2 >= X**2 + Y**2:
            print(i)
            break