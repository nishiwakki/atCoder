# -*- coding: UTF-8 -*-

# INPUT
N = int(input())
S = input()
next_o, next_x = [], []
index_o, index_x = -1, -1
for i in range(N-1, -1, -1):
    if S[i] == 'o':
        next_o.append(-1)
        next_x.append(index_x)
        index_o = i
    else:
        next_o.append(index_o)
        next_x.append(-1)
        index_x = i
next_o.reverse()
next_x.reverse()
ans = 0
for i in range(N-1):
    if S[i] == 'o':
        if not next_x[i] == -1:
            ans += N - next_x[i]
    else:
        if not next_o[i] == -1:
            ans += N - next_o[i]
# OUTPUT
print(ans)