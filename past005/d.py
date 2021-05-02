# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~~~~~~
- pythonのソートは安定性があることを利用
1. 先頭につく0の個数が大きい順にソート
2. Sを10進数の値と見た際の小さい順にソート
~~~~~~~~~~~~~~~~~~~~~~~~~'''

import sys
input = sys.stdin.readline

# 先頭につく0の個数をカウントする関数
def cnt_zero(S):
    cnt = 0
    for s in S:
        if s == '0':
            cnt += 1
        else:
            break
    return cnt

N = int(input())
S = []
for i in range(N):
    s = input().rstrip('\n')
    # (先頭につく0の個数, 10進数の値, 文字列S)
    S.append((cnt_zero(s), int(s), s))
# 第1ソート
S.sort(reverse=True)
# 第2ソート
S.sort(key=lambda x:x[1])
# 出力
for s in S:
    print(s[2])