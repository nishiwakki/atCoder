# -*- coding: UTF-8 -*-

import itertools # 累積和で使用

# 入力
N = int(input())
A = list(map(int, input().split()))

# Aの累積和
cumsum = list(itertools.accumulate(A))
# そこまでのidxの累積和最大値をリスト化
cumsum_max = [cumsum[0]]
for i in range(1, N):
    cumsum_max.append(max(cumsum_max[i-1], cumsum[i]))

# 出力する最大値を保管。最低でも0が保証されている
ans = 0
val = 0
# 累積和を左から順に1つずつ足していく
for i in range(N):
    # i回目の動作前までの座標を取得
    val += cumsum[i] - A[i]
    # i回目までの座標最大値を加算して、最大値を更新
    ans = max(ans, val + cumsum_max[i])
# 出力
print(ans)

'''
[N]
3
[A]
-1 -2 9
[cumsum]
-1 -3 6
[cumsum_max]
-1 -1 6

-1
-2 -4
-5 -7 2
'''