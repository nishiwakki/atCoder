# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
A - B = C は, A = B + C
L ≦ B, C より, 2L ≦ A ≦ R
A は整数より, R - 2L < 0 は0通り
2L ≦ A ≦ R (A:整数) 間でのAについて,
(例) (L, R) = (2, 6)
2L=4: (B, C) = (2, 2)
   5: (B, C) = (2, 3), (3, 2)
 R=6: (B, C) = (2, 4), (3, 3), (4, 2)
- Aは R - 2L + 1 通り
- Aが1増えると, B,Cの組合せも1ずつ増える
~~~~~~~~~~~~~~~~~~~~'''

import sys
input = sys.stdin.readline

# テストケース数
T = int(input())
for _ in range(T):
    # 入力
    L, R = map(int, input().split())
    # 出力
    if R - L * 2 < 0:
        print(0)
    else:
        print((1+(R-L*2+1))*(R-L*2+1)//2)