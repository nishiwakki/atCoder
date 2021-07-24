# -*- coding: UTF-8 -*-

MOD = 10**9 + 7

S = list(input())
c, ch, cho, chok = 0, 0, 0, 0
choku, chokud, chokuda = 0, 0, 0
ans = 0
for i in range(len(S)):
    if S[i] == 'c':
        c += 1
    elif S[i] == 'h':
        ch += c
    elif S[i] == 'o':
        cho += ch
    elif S[i] == 'k':
        chok += cho
    elif S[i] == 'u':
        choku += chok
    elif S[i] == 'd':
        chokud += choku
    elif S[i] == 'a':
        chokuda += chokud
    elif S[i] == 'i':
        ans += chokuda
        ans %= MOD
print(ans)