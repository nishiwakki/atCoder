# -*- coding: UTF-8 -*-

from collections import deque

# 入力
Sa = deque(input())
Sb = deque(input())
Sc = deque(input())
# 最初は A のターン
next = 'a'
# シミュレート
for i in range(350):
    if next == 'a':
        if len(Sa) > 0:
            next = Sa.popleft()
        else:
            print('A')
            exit()
    elif next == 'b':
        if len(Sb) > 0:
            next = Sb.popleft()
        else:
            print('B')
            exit()
    else:
        if len(Sc) > 0:
            next = Sc.popleft()
        else:
            print('C')
            exit()