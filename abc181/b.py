# -*- coding: UTF-8 -*-

N = int(input())
# 答え
ans = 0 
for i in range(N):
    a, b = map(int, input().split())
    # a~bまでの総和をansに加算
    ans += (a+b) * (b-a+1) // 2
print(ans)