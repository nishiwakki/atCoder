# -*- coding: UTF-8 -*-

x, y = map(int, input().split())
# 2人が同じならもう一人も同じであいこ
if x == y:
    print(x)
# 3人とも異なる
else:
    print(3-x-y)