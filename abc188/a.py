# -*- coding: UTF-8 -*-

# 入力
X, Y = map(int, input().split())
# X, Yの差が3ポイント未満か?
# 出力
if abs(X-Y) < 3:
    print('Yes')
else:
    print('No')