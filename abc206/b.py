# -*- coding: UTF-8 -*-

N = int(input())
money = 0
for date in range(1, 100000000):
    money += date
    if money >= N:
        print(date)
        break