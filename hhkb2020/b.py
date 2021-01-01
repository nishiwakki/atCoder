# -*- coding: UTF-8 -*-

# 入力
H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(list(input()))
# 選び方をカウントする変数
ans = 0
# 横の選び方をサーチ
for h in range(H):
    for w in range(W-1):
        # 連続する散らかっていない場所が対象
        if S[h][w] == '.' and S[h][w+1] == '.':
            ans += 1
# 縦の選び方をサーチ
for w in range(W):
    for h in range(H-1):
        # 連続する散らかっていない場所が対象
        if S[h][w] == '.' and S[h+1][w] == '.':
            ans += 1
# 出力
print(ans)