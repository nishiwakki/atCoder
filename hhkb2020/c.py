# -*- coding: UTF-8 -*-

# 入力
N = int(input())
p = list(map(int, input().split()))
# 0 ~ 200000の整数出現回数をカウント
num = [0] * 200001
# 最小値を保持
min_p = 0
for i in range(N):
    # piが最小値と同値のとき
    if min_p == p[i]:
        # 最小値より大きい値でまだ出現してない値をサーチ
        for j in range(min_p+1, 200002):
            if num[j] == 0:
                min_p = j
                break
    else:
        num[p[i]] += 1
    # 出力
    print(min_p)