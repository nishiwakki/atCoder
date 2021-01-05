# -*- coding: UTF-8 -*-

# 入力
N, S = map(str, input().split())
N = int(N)
# [例外処理]
# N=1のときは必ず0
if N == 1:
    print(0)
    exit()
# 条件を満たすTの個数
ans = 0
# Tの長さが奇数のとき条件を必ず満たさない
for i in range(2, N+1, 2):
    # A: +1, T: -1
    AT = 0
    # C: +1, G: -1
    CG = 0
    # Sの0文字目 ~ i-1文字目までをチェック
    for j in range(i):
        if S[j] == 'A':
            AT += 1
        elif S[j] == 'T':
            AT -= 1
        elif S[j] == 'C':
            CG += 1
        else:
            CG -= 1
    # 条件を満たすとき
    if AT == 0 and CG == 0:
        ans += 1
    # Sのi文字目 ~ N-1文字目まで
    # 1文字ずつずらしながらチェック
    for j in range(i, N):
        # 右にずれて追加される文字
        if S[j] == 'A':
            AT += 1
        elif S[j] == 'T':
            AT -= 1
        elif S[j] == 'C':
            CG += 1
        else:
            CG -= 1
        # 右にずれて削除される文字
        if S[j-i] == 'A':
            AT -= 1
        elif S[j-i] == 'T':
            AT += 1
        elif S[j-i] == 'C':
            CG -= 1
        else:
            CG += 1
        # 条件を満たすとき
        if AT == 0 and CG == 0:
            ans += 1
# 出力
print(ans)