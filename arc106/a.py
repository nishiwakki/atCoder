# -*- coding: UTF-8 -*-

# 入力
N = int(input())
# 全探索(正の整数なので1~)
for A in range(1, 50):
    for B in range(1, 50):
        # 見つかった場合は出力
        if 3**A + 5**B == N:
            print(A, B)
            exit()
# 見つからない場合-1を出力
print(-1)