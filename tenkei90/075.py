# -*- coding: UTF-8 -*-

def prime_factorize(n):
    ret = []
    for div in range(2, int(n**0.5)+1):
        while n % div == 0:
            ret.append(div)
            n //= div
    if not n == 1:
        ret.append(n)
    return ret

N = int(input())
cnt = len(prime_factorize(N))
for i in range():
    if cnt <= 2**i:
        print(i)
        break