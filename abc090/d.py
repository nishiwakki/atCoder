# -*- coding: UTF-8 -*-

'''
[例] N = 14, K = 5 で考える
この場合, a % bが5以上になるためには,
まず 6 以上で a を割る必要がある. (K+1以上)
div = 6 と固定して考えたとき,
ありうる a の値について次の通りになる.
~ div = 6 ~
[a]       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
[a%6]     0 1 2 3 4 5 0 1 2 3  4  5  0  1  2
[a%6>=5]  x x x x x o x x x x  x  o  x  x  x

div = 7でも同様に考えてみる.
~ div = 7 ~
[a]       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
[a%7]     0 1 2 3 4 5 6 0 1 2  3  4  5  6  0
[a%7>=5]  x x x x x o o x x x  x  x  o  o  x
'''

# 入力
N, K = map(int, input().split())
# 該当組の個数
ans = 0
# a を K+1 以上 N 以下で除算すると,余りが K 以上になる可能性あり
for div in range(K+1, N+1):
    ans += N - K * (N // div) - min(max(0, K-1), N % div)
# 出力
print(ans)