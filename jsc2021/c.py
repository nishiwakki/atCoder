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
    return low_div + high_div

MAX = 2*(10**5) + 1
A, B = map(int, input().split())
# cnt[i]
# A以上B以下の整数xの約数iを持つ回数
cnt = [0] * MAX
for i in range(A, B+1):
    for d in divisor(i):
        cnt[d] += 1
ans = 0
for i in range(MAX):
    if cnt[i] > 1:
        ans = i
print(ans)