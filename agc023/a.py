# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
EX1の 配列a と その累積和A は次の通り
a:    1,  3, -4,  2,  2, -2
A: 0, 1,  4,  0,  2,  4,  2
これより,配列aの部分列の総和
は次のように求められる.
[1]        A[1] - A[0]
[1 3]      A[2] - A[0]
[3]        A[2] - A[1]
[1 3 -4]   A[3] - A[0]
[3 -4]     A[3] - A[1]
[-4]       A[3] - A[2]
[1 3 -4 2] A[4] - A[0]
[3 -4 2]   A[4] - A[1]
[-4 2]     A[4] - A[2]
[2]        A[4] - A[3]
~~~~~~~~~~~~~~~~~~~~'''

from itertools import accumulate
from collections import defaultdict

N = int(input())
A = [0] + list(accumulate(map(int, input().split())))
ans = 0
dd = defaultdict(int)
for i in range(1, N+1):
    dd[A[i-1]] += 1
    ans += dd[A[i]]
print(ans)