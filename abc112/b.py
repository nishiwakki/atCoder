# -*- coding: UTF-8 -*-

# 入力
N, T = map(int, input().split())
# 最小経路のコスト(1 <= t <= 1000)
ans = 1001
for i in range(N):
    c, t = map(int, input().split())
    # 時間T以内のとき
    if t <= T:
        # 最小コストを更新
        ans = min(ans, c)
# 出力
# ansが更新されないときTLE
if ans == 1001:
    print('TLE')
else:
    print(ans)