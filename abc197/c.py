# -*- coding: UTF-8 -*-

from itertools import product

N = int(input())
A = list(map(int, input().split()))
if N == 1:
    print(A[0])
    exit()
ans = float('inf')
# 区間分けできるN-1箇所を全探索
for pat in product(range(2), repeat=N-1):
    Xor = -1
    Or = A[0]
    for i, p in enumerate(pat):
        # p=1(区切る)
        if p:
            if Xor == -1:
                Xor = Or
            else:
                Xor ^= Or
            Or = A[i+1]
        # p=0(区切らない)
        else:
            Or |= A[i+1]
    if Xor == -1:
        Xor = Or
    else:
        Xor ^= Or
    ans = min(ans, Xor)
print(ans)