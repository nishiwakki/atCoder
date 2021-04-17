# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
               1 ≦ i ≦             999 : 0
            10^0                10^3-1
            1000 ≦ i ≦          999999 : 1
            10^3                10^6-1
         1000000 ≦ i ≦       999999999 : 2
            10^6                10^9-1
      1000000000 ≦ i ≦    999999999999 : 3
            10^9               10^12-1
   1000000000000 ≦ i ≦ 999999999999999 : 4
           10^12               10^15-1
1000000000000000 = i                   : 5
           10^15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

N = int(input())
ans = 0
if N > 10**3-1:
    ans += N - 10**3 + 1
if N > 10**6-1:
    ans += N - 10**6 + 1
if N > 10**9-1:
    ans += N - 10**9 + 1
if N > 10**12-1:
    ans += N - 10**12 + 1
if N == 10**15:
    ans += 1
print(ans)