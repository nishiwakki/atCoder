# -*- coding: UTF-8 -*-

def divisor(n):
    low_div, high_div = [], []
    i = 1
    while i*i <= n:
        if not n % i:
            low_div.append(i)
            if not i == n//i:
                high_div.append(n//i)
        i += 1
    return low_div + high_div[::-1]

# INPUT
K = int(input())
# 約数列挙
divs = divisor(K)
ans = 0
for ai in range(len(divs)):
    for bi in range(ai, len(divs)):
        a, b = divs[ai], divs[bi]
        if not K % (a*b) == 0:
            continue
        c = K // a // b
        if not a <= b <= c:
            continue
        ans += 1
# OUTPUT
print(ans)