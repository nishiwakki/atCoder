# -*- coding: UTF-8 -*-

# 入力
N, K = map(int, input().split())
a = list(map(int, input().split()))
# ボールに書かれている数でカウント
balls = [0] * (N+1)
for i in a:
    balls[i] += 1
# 最大値を保持
ans = 0
# 0, 1,...i までの数の
# ボールが入った箱を作れる総数
k = K
for i in range(N):
    ans += i * max(0, k-balls[i])
    # kを更新
    k = min(k, balls[i])
if k > 0:
    ans += N * k
# 出力
print(ans)