# -*- coding: UTF-8 -*-

# 入力
X = int(input())
A = int(input())
B = int(input())
# ケーキを買う
X -= A
# ドーナツを買う
X %= B
# 出力
print(X)