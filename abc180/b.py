# -*- coding: UTF-8 -*-

# 入力
N = int(input())
x = list(map(int, input().split()))

manhat = 0
euclid = 0
chebys = 0
for i in x:
    manhat += abs(i)
    euclid += i ** 2
    chebys = max(chebys, abs(i))
# 出力
print(manhat)
print(euclid ** 0.5)
print(chebys)