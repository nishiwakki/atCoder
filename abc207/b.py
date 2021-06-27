# -*- coding: UTF-8 -*-

A, B, C, D = map(int, input().split())
blue, red = A, 0
ans = -1
for i in range(A):
    blue += B
    red += C
    if blue <= D*red:
        ans = i + 1
        break
print(ans)