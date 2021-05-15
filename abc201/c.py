# -*- coding: UTF-8 -*-

from itertools import product

S = input()
co = [i for i in range(10) if S[i] == 'o']
cx = [i for i in range(10) if S[i] == 'x']
cq = [i for i in range(10) if S[i] == '?']
ans = 0
for p in product(range(10), repeat=4):
    flg = True
    for cc in co:
        if not cc in p:
            flg = False
    for cc in cx:
        if cc in p:
            flg = False
    if not flg:
        continue
    ans += 1
print(ans)