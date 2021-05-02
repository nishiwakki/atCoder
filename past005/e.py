# -*- coding: UTF-8 -*-

# ハンコを90度時計回りに回転する関数
def rot_x_to_y(h, w, G):
    retG = [[''] * h for _ in range(w)]
    for i in range(h):
        for j in range(w):
            retG[j][h-i-1] = G[i][j]
    return retG

# 入力
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]

# [step1]
# ハンコTの余計な部分をカットする
top, bot = 0, H
for x in range(H):
    if not T[x].count('#'):
        top = x+1
    else:
        break
for x in range(H-1, -1, -1):
    if not T[x].count('#'):
        bot = x
    else:
        break
lef, rig = 0, W
for y in range(W):
    cnt = 0
    for x in range(H):
        if T[x][y] == '#':
            cnt += 1
    if not cnt:
        lef = y+1
    else:
        break
for y in range(W-1, -1, -1):
    cnt = 0
    for x in range(H):
        if T[x][y] == '#':
            cnt += 1
    if not cnt:
        rig = y
    else:
        break
# 余分をカットしたnewハンコT
T = [T[h][lef:rig] for h in range(top, bot)]
# newハンコTの大きさ
TH, TW = bot-top, rig-lef

# [step2]
# マス目SにハンコTを押せるか全探索
ans = False
# 4方向を試す
for a in range(4):
    # a=0以外はハンコTを回転させる
    if a:
        S = rot_x_to_y(H, W, S)
        H, W = W, H
    # ハンコTがマス目Sより小さい分だけ
    # 位置をずらして押しまくる探索
    for x in range(H-TH+1):
        for y in range(W-TW+1):
            flg = True
            for i in range(TH):
                for j in range(TW):
                    # 1箇所でも両方凸('#')だとダメ
                    if S[i+x][j+y] == '#' and T[i][j] == '#':
                        flg = False
            # 1パターンでもいけるならOK
            if flg:
                ans = True
# 出力
if ans:
    print('Yes')
else:
    print('No')