# -*- coding: UTF-8 -*-

'''
入力例1について
c1 = max(a1*b1)
c2 = max(c1, a1*b2, a2*b2)
c3 = max(c2, a1*b3, a2*b3, a3*b3)
となるため、c[i]について
- c[i-1]
- a[0]~a[i]の最大値 と b[i]の積
の大きい方が最大値となる
'''

# 入力
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_max = a[0]
c_max = 0
for i in range(N):
    a_max = max(a_max, a[i])
    c_max = max(c_max, a_max * b[i])
    # 出力
    print(c_max)