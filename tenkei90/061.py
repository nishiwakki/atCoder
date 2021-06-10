# -*- coding: UTF-8 -*-

from collections import deque
import sys
input = sys.stdin.readline

deck = deque()
Q = int(input())
for q in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        deck.appendleft(x)
    elif t == 2:
        deck.append(x)
    else:
        print(deck[x-1])