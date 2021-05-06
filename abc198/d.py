# -*- coding: UTF-8 -*-

from itertools import permutations

def make_num(ls):
    ret = 0
    for i, j in enumerate(ls):
        ret += j * 10**i
    return ret

S1 = input()[::-1]
S2 = input()[::-1]
S3 = input()[::-1]
s = list(set(S1+S2+S3))
if len(s) <= 10:
    for p in permutations(range(10), len(s)):
        ls1 = [p[s.index(S)] for S in S1]
        ls2 = [p[s.index(S)] for S in S2]
        ls3 = [p[s.index(S)] for S in S3]
        if ls1[-1] == 0 or ls2[-1] == 0 or ls3[-1] == 0:
            continue
        N1 = make_num(ls1)
        N2 = make_num(ls2)
        N3 = make_num(ls3)
        if N1 + N2 == N3:
            print(N1)
            print(N2)
            print(N3)
            exit()
print('UNSOLVABLE')