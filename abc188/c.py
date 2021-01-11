# -*- coding: UTF-8 -*-

# 入力
N = int(input())
A = list(map(int, input().split()))
# 前半部、後半部の最大レート
max_1st = max(A[0 : 2**(N-1)])
max_2nd = max(A[2**(N-1) : 2**N])
# 出力(2番目のindex+1を出力)
if max_1st < max_2nd:
    print(A.index(max_1st) + 1)
else:
    print(A.index(max_2nd) + 1)