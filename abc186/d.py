# -*- coding: UTF-8 -*-

'''
入力例2
-----
5
31 41 59 26 53
-----
求めるのは絶対値なので、
Aの要素を並べ替えても問題ない。
降順ソートを行う。
  59 53 41 31 26
1巡目は
  (59-53)+(59-41)+(59-31)+(59-26)
という考え方をすると、これは
  59*4 - (53+41+31+26)
と同義である。
'''

# 入力
N = int(input())
A = list(map(int, input().split()))
# Aの合計を算出
sum_A = sum(A)
# Aを降順ソート　
A.sort(reverse=True)
# 答えの値を保持
ans = 0
for i in range(N-1):
    ans += A[i] * (N-i) - sum_A
    sum_A -= A[i]
# 出力
print(ans)