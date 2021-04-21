# -*- coding: UTF-8 -*-

N = int(input())
A, B, C = map(int, input().split())
ans = 10000
for a in range(10000):
    for b in range(10000):
        rem = N - A*a - B*b
        if rem < 0:
            break
        if not rem % C:
            ans = min(ans, a+b+rem//C)
print(ans)