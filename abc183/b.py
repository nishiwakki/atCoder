# -*- coding: UTF-8 -*-

# 入力
Sx, Sy, Gx, Gy = map(int, input().split())
# SxからのAxのx差分
diffx = (Gx - Sx) * (Sy / (Sy + Gy))
ans = Sx + diffx
# 出力
print(ans)