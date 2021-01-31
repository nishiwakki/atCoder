# -*- coding: UTF-8 -*-

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
N = int(input())
# Nの約数列挙
divs = divisor(N)
# 奇数の約数をカウント
ans = 0
for div in divs:
    # 奇数なら
    if div % 2:
        ans += 1
# 出力
print(ans * 2)