# -*- coding: UTF-8 -*-

# 入力
N = int(input())
x, y, h = [0]*N, [0]*N, [0]*N
for i in range(N):
    x[i], y[i], h[i] = map(int, input().split())
# 0 <= Cx <= 100 の101通り全探索
for Cx in range(101):
    # 0 <= Cy <= 100 の101通り全探索
    for Cy in range(101):
        for i in range(N):
            # 必ず h[i] > 0 を満たす情報が1つ以上ある
            # h[i] = 0 はmax関数で落ちる可能性があるため不可
            if not h[i]:
                continue
            # ピラミッドの高さH を決め打ち
            H = h[i] + abs(x[i]-Cx) + abs(y[i]-Cy)
        # 情報と矛盾が生じるなら False
        check = True
        # 情報について N全通り全探索
        for i in range(N):
            # 情報 i 番目の座標(x, y)から高度を計算
            hh = max(H - abs(Cx-x[i]) - abs(Cy-y[i]), 0)
            # 情報 i 番目の高度 hi と一致しないなら矛盾
            if not h[i] == hh:
                check = False
        # 全ての情報と矛盾が起こらないとき
        if check:
            # 出力
            print(Cx, Cy, H)