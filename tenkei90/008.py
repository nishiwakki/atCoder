# -*- coding: UTF-8 -*-

MOD = 10**9 + 7

N = int(input())
S = input()
a, at, atc, atco = 0, 0, 0, 0
atcod, atcode, ans = 0, 0, 0
for s in S:
    if s == 'a':
        a += 1
    elif s == 't':
        at += a
    elif s == 'c':
        atc += at
    elif s == 'o':
        atco += atc
    elif s == 'd':
        atcod += atco
    elif s == 'e':
        atcode += atcod
    elif s == 'r':
        ans = (ans + atcode) % MOD
print(ans)