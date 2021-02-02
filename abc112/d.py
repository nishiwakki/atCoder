# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
[入力例1]で考えてみる. (N, M) = (3, 14)
14の約数は, 1, 2, 7, 14 であり, 
- 14 *  1 = 14 (14)
-  7 *  2 = 14 (7+7)
-  2 *  7 = 14 (2+2+2+2+2+2+2)
-  1 * 14 = 14 (1+1+1+...+1+1)
と表せる. 上の2式は N = 3 より
a1 + a2 + ... + aN = M の式で表せないが,
下の2式は, 余分な足し算を他にくっつけることで表せる.
(2*7=14)  2 + 2 + 10 = 14
(1*14=14) 1 + 1 + 12 = 14
上の例だと, 10 も当然 2 で割り切れ, G.C.d = 2 とできる.
~~~~~~~~~~~~~~~~~~~~'''

# 約数列挙
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

# 入力
N, M = map(int, input().split())
# Mの約数でリスト作成
divs = divisor(M)
for div in divs:
    if div >= N:
        # 出力
        print(M // div)
        break