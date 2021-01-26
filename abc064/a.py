# -*- coding: UTF-8 -*-

# 入力
r, g, b = map(int, input().split())
# 出力
# 4の倍数か
if (100*r + 10*g + b) % 4 == 0:
    print('YES')
else:
    print('NO')