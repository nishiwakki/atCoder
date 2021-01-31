# -*- coding: UTF-8 -*-

# 入力
A, B, C = map(int, input().split())
# 出力
# 同個数のとき
if A == B:
    # Cによって決まる
    if C:
        print('Takahashi')
    else:
        print('Aoki')
# 個数が異なるとき
else:
    # 多い方が勝つ
    if A > B:
        print('Takahashi')
    else:
        print('Aoki')