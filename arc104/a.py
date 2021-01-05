# -*- coding: UTF-8 -*-

# 入力
A, B = map(int, input().split())
# A+B = (X+Y)+(X-Y) = 2X
# A-B = (X+Y)-(X-Y) = 2Y
X = (A+B) // 2
Y = (A-B) // 2
# 出力
print(X, Y)