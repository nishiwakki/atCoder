# -*- coding: UTF-8 -*-

A, B = map(int, input().split())
ans = []
amari = 0
if A >= B:
    cnt = B-1
    for i in range(1, A+1):
        ans.append(i)
        if cnt:
            ans.append(-i)
            cnt -= 1
        else:
            amari += -i
    ans.append(amari)
else:
    cnt = A-1
    for i in range(1, B+1):
        ans.append(-i)
        if cnt:
            ans.append(i)
            cnt -= 1
        else:
            amari += i
    ans.append(amari)
print(*ans)