# -*- coding: UTF-8 -*-

import sys
input = sys.stdin.readline

# 入力
N = int(input())
# 行の交換情報を保持
row = [i for i in range(N)]
# 列の交換情報を保持
col = [i for i in range(N)]
# 答え
ans = []
# 転置回数(Query3)
cnt3 = 0
# クエリ数
Q = int(input())
# クエリ処理
for q in range(Q):
    query = list(map(int, input().split()))
    # 1 A B
    if query[0] == 1:
        A, B = query[1]-1, query[2]-1
        # 転置回数が奇数
        if cnt3 % 2:
            col[A], col[B] = col[B], col[A]
        else:
            row[A], row[B] = row[B], row[A]
    # 2 A B
    elif query[0] == 2:
        A, B = query[1]-1, query[2]-1
        if cnt3 % 2:
            row[A], row[B] = row[B], row[A]
        else:
            col[A], col[B] = col[B], col[A]
    # 3
    elif query[0] == 3:
        cnt3 += 1
    # 4 A B
    else:
        A, B = query[1]-1, query[2]-1
        if cnt3 % 2:
            i, j = row[B], col[A]
        else:
            i, j = row[A], col[B]
        ans.append(N * i + j)
# 出力
for a in ans:
    print(a)