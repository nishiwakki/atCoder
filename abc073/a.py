# -*- coding: UTF-8 -*-

# 入力
N = int(input())
# 出力
# 一の桁が9 or 十の桁が9 なら
if N % 10 == 9 or N // 10 == 9:
    print('Yes')
else:
    print('No')