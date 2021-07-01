# -*- coding: UTF-8 -*-

from math import degrees, radians, sin, cos, atan2

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for q in range(Q):
    E = int(input())
    # E分後の観覧車のy座標
    y = -L * sin(radians(360*E/T)) / 2
    # E分後の観覧車のz座標
    z = (L-L*cos(radians(360*E/T))) / 2
    # 観覧車~像の 高さの差 と 水平距離 を算出
    ans = degrees(atan2(z, (X**2+(y-Y)**2)**0.5))
    print(ans)