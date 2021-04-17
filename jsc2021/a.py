# -*- coding: UTF-8 -*-

X, Y, Z = map(int, input().split())
ans = 0
for i in range(10**6+1):
    if Y/X > i/Z:
        ans = i
    else:
        break
print(ans)