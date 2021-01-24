# -*- coding: UTF-8 -*-

'''-----
[入力例]
4
2 4 9 4
*
* *
* * *
* * * *
  -
  - -
  - - -
    +
    + +
      /
-----'''

# 入力
N = int(input())
A = list(map(int, input().split()))
# 最大値を保持
ans = 0
# 左端を固定
for l in range(N):
    min_sec = A[l]
    # rを1つずつ右にずらす
    for r in range(l, N):
        min_sec = min(min_sec, A[r])
        # 最大値を更新
        ans = max(ans, min_sec*(r-l+1))
# 出力
print(ans)