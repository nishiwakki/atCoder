# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
  [コンプガチャ問題]
  確率 p(p≠0) で成功する試行を,
  成功するまでの試行回数の期待値は,
    1/p
~~~~~~~~~~~~~~~~~~~~'''

# 入力
N = int(input())
# 答え　
ans = 0
for i in range(1, N):
    ans += N / i
# 出力
print(ans)