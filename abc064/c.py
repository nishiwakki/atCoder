# -*- coding: UTF-8 -*-

# 入力
N = int(input())
a = list(map(int, input().split()))
# 0: 灰, 1:茶, ... 7: 赤, 8: 自由 の人数
color = [0] * 9
# 3600以上 は color[8]に +1
for i in a:
    color[min(i//400, 8)] += 1
ans = 0
# 各色について
for i in range(9):
    # 3200未満の人がいないとき, 最小値に要注意
    if i == 8:
        # 出力
        print(max(1, ans), ans+color[8])
    # 0~3199までは該当する人がいるなら +1
    else:
        if color[i]:
            ans += 1