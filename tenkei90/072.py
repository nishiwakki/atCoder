# -*- coding: UTF-8 -*-

# 入力
H, W = map(int, input().split())
c = [list(input()) for h in range(H)]
# 答えの最大値を保持(初期値: -1)
ans = -1

def DFS(nh, nw, sh, sw):
    # 再帰関数内でも 最大値 を更新できるように
    global ans
    # 隣接マスが始点かどうか
    if nh == sh:
        if (nw+1 == sw) or (nw-1 == sw):
            if len(route) >= 3:
                ans = max(ans, len(route))
    if nw == sw:
        if (nh+1 == sh) or (nh-1 == sh):
            if len(route) >= 3:
                ans = max(ans, len(route))
    # DOWN
    if nh < H-1 and c[nh+1][nw] == '.' and seen[nh+1][nw]:
        seen[nh+1][nw] = False
        route.append((nh+1, nw))
        DFS(nh+1, nw, sh, sw)
    # UP
    if nh > 0 and c[nh-1][nw] == '.' and seen[nh-1][nw]:
        seen[nh-1][nw] = False
        route.append((nh-1, nw))
        DFS(nh-1, nw, sh, sw)
    # RIGHT
    if nw < W-1 and c[nh][nw+1] == '.' and seen[nh][nw+1]:
        seen[nh][nw+1] = False
        route.append((nh, nw+1))
        DFS(nh, nw+1, sh, sw)
    # LEFT
    if nw > 0 and c[nh][nw-1] == '.' and seen[nh][nw-1]:
        seen[nh][nw-1] = False
        route.append((nh, nw-1))
        DFS(nh, nw-1, sh, sw)
    # BACK-TRACK
    h, w = route.pop()
    seen[h][w] = True

# 各マスを始点としたとき
for h in range(H):
    for w in range(W):
        # 山マスは始点にならない
        if c[h][w] == '#':
            continue
        seen = [[True] * W for h in range(H)]
        seen[h][w] = False
        route = [(h, w)]
        DFS(h, w, h, w)
# 出力
print(ans)