# -*- coding: UTF-8 -*-

# 入力
N = int(input())
a = [list(input()) for _ in range(N)]
# 答え
ans = [''] * N
# 奇数文字なら
if N % 2:
    # 真ん中の文字はなんでも良い
    ans[N//2] = a[N//2][0]
for i in range(N//2):
    # 対のindex
    j = N - i - 1
    # 共通文字
    common = set(a[i]) & set(a[j])
    # ある場合
    if common:
        c = common.pop()
        ans[i], ans[j] = c, c
    # ないなら存在しない
    else:
        print('-1')
        exit()
# 出力
print(''.join(ans))