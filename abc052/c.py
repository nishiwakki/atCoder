# -*- coding: UTF-8 -*-

# [Example]
# prime_factorize(12)
# -> [2, 2, 3] 
def prime_factorize(n):
    ret = []
    for div in range(2, int(n**0.5)+1):
        while n % div == 0:
            ret.append(div)
            n //= div
    if not n == 1:
        ret.append(n)
    return ret

MOD = 10**9 + 7
# 入力
N = int(input())
ans = 1
# N!を構成する素数とその個数を管理
prime_dict = {}
for i in range(1, N+1):
    # i の素数を列挙
    primes = prime_factorize(i)
    # 各素数に対して
    for p in primes:
        # prime_dictに既に存在する素数か?
        if p in prime_dict:
            # 個数 + 1
            prime_dict[p] = prime_dict[p] + 1
        else:
            # 追加して個数 1 とする
            prime_dict[p] = 1
# 各素数の個数を取り出して計算
for v in prime_dict.values():
    ans = ans * (v+1) % MOD
# 出力
print(ans)