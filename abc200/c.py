# -*- coding: UTF-8 -*-

N = int(input())
A = list(map(int, input().split()))
cnt = [0] * 201
for a in A:
    cnt[a%200] += 1
ans = 0
for i in cnt:
    ans += i*(i-1)//2
print(ans)