# -*- coding: UTF-8 -*-

# 入力
H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
# コインの移動
ans = []
# 各行について(1 <= i <= H-1)
for i in range(H-1):
    # 各列について(1 <= j <= W)
    for j in range(W):
        # 奇数個なら下にコインを移動
        if a[i][j] % 2:
            a[i+1][j] += 1
            ans.append([i+1, j+1, i+2, j+1])
# 最下行について(i = H)
for j in range(W-1):
    # 奇数個なら右にコインを移動
    if a[H-1][j] % 2:
        a[H-1][j+1] += 1
        ans.append([H, j+1, H, j+2])
# 出力
print(len(ans))
for i in ans:
    print(*i)