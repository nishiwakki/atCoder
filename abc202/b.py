# -*- coding: UTF-8 -*-

S = list(input())[::-1]
ans = []
for s in S:
    if s == '6':
        ans.append('9')
    elif s == '9':
        ans.append('6')
    else:
        ans.append(s)
print(''.join(ans))