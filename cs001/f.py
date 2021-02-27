# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
数列 a における各数値について,
その数値よりも左に大きい数値がない場合,
+1 せよ.
(例) 3 1 5 4 2
3: 3が最大なので +1
1: 3が最大なので 変化無し
5: 5が最大なので +1
4: 5が最大なので 変化無し
2: 5が最大なので 変化無し
~~~~~~~~~~~~~~~~~~~~'''

# 入力
N = int(input())
A = list(map(int, input().split()))
# 答え, 最大数を 0 で初期化
ans, M = 0, 0
# 各数値について
for a in A:
    if a > M:
        M = a
        ans += 1
# 出力
print(ans)