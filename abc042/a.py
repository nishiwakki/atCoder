# -*- coding: UTF-8 -*-

# 入力
ABC = list(map(int, input().split()))
# ソート
ABC.sort()
# 出力
# [5, 5, 7]の形しかありえない
if ABC == [5, 5, 7]:
    print('YES')
else:
    print('NO')