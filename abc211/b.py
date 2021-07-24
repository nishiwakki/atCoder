# -*- coding: UTF-8 -*-

S = [input() for i in range(4)]
if S.count('H') == 1:
    if S.count('2B') == 1:
        if S.count('3B') == 1:
            if S.count('HR') == 1:
                print('Yes')
                exit()
print('No')