# -*- coding: UTF-8 -*-

# 入力
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
# 角を形成する数
ans = 0
for h in range(H-1):
    for w in range(W-1):
        arr = [S[h][w], S[h+1][w], S[h][w+1], S[h+1][w+1]]
        cnt = arr.count('#')
        # 周囲4マス中, '#'の数が 1 or 3 のとき角を形成
        if cnt % 2: 
            ans += 1
# 出力
print(ans)