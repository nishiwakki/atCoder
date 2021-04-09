# -*- coding: UTF-8 -*-

from math import radians, sin, cos

N = int(input())
x0, y0 = map(int, input().split())
xN2, yN2 = map(int, input().split())
# 中心
xc, yc = (x0+xN2) / 2, (y0+yN2) / 2
# ラジアン
rad = radians(360 / N)
# x1, y1について
x1 = (x0-xc) * cos(rad) - (y0-yc) * sin(rad) + xc
y1 = (x0-xc) * sin(rad) + (y0-yc) * cos(rad) + yc
print(x1, y1)