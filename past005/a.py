# -*- coding: UTF-8 -*-

S = input()
if S[0] == S[1] == S[2]:
    print(S[0])
elif S[1] == S[2] == S[3]:
    print(S[1])
elif S[2] == S[3] == S[4]:
    print(S[2])
else:
    print('draw')