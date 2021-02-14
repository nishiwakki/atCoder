# -*- coding: UTF-8 -*-

# 入力
N = int(input())
a = list(map(int, input().split()))
# コストを無限大に設定
ans = 10 ** 9
# -100 ~ 100 まで全探索
for i in range(-100, 101):
    val = 0
    for j in range(N):
        val += (a[j] - i) ** 2
    # 最小コスト更新
    ans = min(ans, val)
# 出力
print(ans)