# -*- coding: UTF-8 -*-

from collections import deque

S = input()
T = deque([])
rev = False
for s in S:
    if s == 'R':
        rev ^= 1
    else:
        if not rev:
            if len(T) > 0 and s == T[-1]:
                T.pop()
            else:
                T.append(s)
        else:
            if len(T) > 0 and s == T[0]:
                T.popleft()
            else:
                T.appendleft(s)
if rev:
    T.reverse()
print(''.join(T))