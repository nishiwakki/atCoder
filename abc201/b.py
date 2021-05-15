# -*- coding: UTF-8 -*-

N = int(input())
ST = []
for i in range(N):
    S, T = map(str, input().split())
    ST.append((int(T), S))
ST.sort(reverse=True)
print(ST[1][1])