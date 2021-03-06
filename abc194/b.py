# -*- coding: UTF-8 -*-

# 入力
N = int(input())
A, B = [], []
for i in range(N):
    a, b = map(int, input().split())
    A.append((a, i))
    B.append((b, i))
# 昇順ソート
A.sort()
B.sort()
# 仕事A最速の人と仕事B最速の人が同じ場合
if A[0][1] == B[0][1]:
    # 出力
    print(
          min(
              A[0][0] + B[0][0], 
              max(A[0][0], B[1][0]), 
              max(A[1][0], B[0][0])
             )
         )
else:
    # 出力
    print(max(A[0][0], B[0][0]))