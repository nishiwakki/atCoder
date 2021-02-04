# -*- coding: UTF-8 -*-

'''
(l, r) = (6, 8) のとき
0123456789
xxxxxxooox
人数は 8 - 6 + 1 = 3 となる
これより r - l + 1 
'''

# 入力
N = int(input())
# 座っている人の数
ans = 0
for i in range(N):
    l, r = map(int, input().split())
    ans += r - l + 1
# 出力
print(ans)