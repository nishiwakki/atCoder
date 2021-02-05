# -*- coding: UTF-8 -*-

# 入力
sx, sy, tx, ty = map(int, input().split())
out_1 = (ty-sy) * 'U' + (tx-sx) * 'R'
ret_1 = (ty-sy) * 'D' + (tx-sx) * 'L'
out_2 = 'L' + (ty-sy+1) * 'U' + (tx-sx+1) * 'R' + 'D'
ret_2 = 'R' + (ty-sy+1) * 'D' + (tx-sx+1) * 'L' + 'U'
# 出力
print(out_1 + ret_1 + out_2 + ret_2)