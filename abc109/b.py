# -*- coding: UTF-8 -*-

# 入力
N = int(input())
# 発言単語リスト
words = []
# 直前に発した単語
prev = None
# TrueならルールOK
ans = True
for i in range(N):
    W = input()
    # i = 0 のとき
    if not i:
        prev = W
    else:
        # 条件2 チェック
        if not prev[-1] == W[0]:
            ans = False
            break
        else:
            # 条件1 チェック
            if W in words:
                ans = False
                break
            prev = W
    words.append(W)
# 出力
if ans:
    print('Yes')
else:
    print('No')