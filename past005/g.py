# -*- coding: UTF-8 -*-

# 返値があるときに一筆書き発見
def dfs(x, y):
    v[x][y] = False
    p.append((x+1, y+1))
    if x > 0 and S[x-1][y] == '#' and v[x-1][y]:
        dfs(x-1, y)
    if x < H-1 and S[x+1][y] == '#' and v[x+1][y]:
        dfs(x+1, y)
    if y > 0 and S[x][y-1] == '#' and v[x][y-1]:
        dfs(x, y-1)
    if y < W-1 and S[x][y+1] == '#' and v[x][y+1]:
        dfs(x, y+1)
    # 上下左右行き止まり時
    # 全て一筆書きできたなら
    if len(p) == k:
        return p
    # このパターンはダメなので一手前に戻す
    else:
        v[x][y] = True
        p.pop()

# 入力
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
# kは'#'の個数
k = sum([s.count('#') for s in S])
# 各マスからDFS
for h in range(H):
    for w in range(W):
        # visited
        v = [[True] * W for _ in range(H)]
        # one-stroke path
        p = []
        # '#'から始まるマスについて
        if S[h][w] == '#':
            res = dfs(h, w)
            if res:
                print(k)
                for x, y in res:
                    print(x, y)
                exit()