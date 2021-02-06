# -*- coding: UTF-8 -*-

# 入力
N = int(input())
S = input()
# 種類数の最大値を 0 で初期化
ans = 0
# 分割位置を全探索
# (1 <= i <= N-1)
for i in range(1, N):
    X, Y = S[0:i], S[i:N]
    # 種類数をカウント
    cnt = 0
    # c[0] = 0: Xに'a'が含まれない
    # c[0] = 1: Xに'a'が含まれる
    c = [0] * 26
    for i in X:
        c[ord(i)-97] = 1
    for i in Y:
        if c[ord(i)-97]:
            cnt += 1
            c[ord(i)-97] = 0
    # 種類数の最大値を更新
    ans = max(ans, cnt)
# 出力
print(ans)