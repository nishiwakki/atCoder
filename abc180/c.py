# -*- coding: UTF-8 -*-

# 約数列挙
def divisor(n):
    i = 1
    ret = []
    while i ** 2 <= n:
        if n % i == 0:
            ret.append(i)
            ret.append(n // i)
        i += 1
    ret = sorted(list(set(ret)))
    return ret

# 入力
N = int(input())
# 約数リスト取得
divList = divisor(N)
for ans in divList:
    print(ans)