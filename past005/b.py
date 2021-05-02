# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~~~~~~
同じ文字ならSの前にある文字は,
全て削除されてしまう.
後ろから見ていって,
Tの中に含まれない文字であれば必ず残る.
~~~~~~~~~~~~~~~~~~~~~~~~~'''

N = int(input())
S = reversed(list(input()))
T = []
for s in S:
    if not s in T:
        T.append(s)
print(''.join(reversed(T)))