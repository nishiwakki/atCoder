# -*- coding: UTF-8 -*-

# 入力
N, A, B = map(int, input().split())
X = list(map(int, input().split()))
# 最小の疲労度を保持
ans = 0
for i in range(1, N):
    # 1つ東の街へ歩いて移動
    walk = (X[i] - X[i-1]) * A
    # 1つ東の街へテレポート
    tele = B
    # 小さい方の疲労度で計算
    ans += min(walk, tele)
# 出力
print(ans)