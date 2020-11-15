# -*- coding: UTF-8 -*-

# 順列生成ライブラリ
from itertools import permutations

# 入力
N, K = map(int, input().split())
T = [None] * N
for i in range(N):
    T[i] = list(map(int, input().split()))
# 2~Nまでの都市番号作成
city = list(range(2, N+1))
# 2~Nまでの都市の経路を全作成
pattern = permutations(city, N-1)
# 出力する答えをカウントアップ
ans = 0
for patt in pattern:
    # 都市1から最初の移動
    time = T[0][patt[0]-1]
    nowCity = patt[0] - 1
    # 各都市から各都市への移動
    for i in range(1, N-1):
        time += T[nowCity][patt[i] - 1]
        nowCity = patt[i] - 1
    # 全都市を回り都市1への移動
    time += T[nowCity][0]
    if time == K:
        ans += 1
# 出力
print(ans)