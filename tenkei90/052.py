# -*- coding: UTF-8 -*-

MOD = 10**9 + 7

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 1
for a in A:
    ans *= sum(a)
    ans %= MOD
print(ans)