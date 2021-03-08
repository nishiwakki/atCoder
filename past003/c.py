# -*- coding: UTF-8 -*-

# 入力
A, R, N = map(int, input().split())
ans = A
# 公比1のとき
if R == 1:
    # 初項が答え
    print(ans)
else:
    # (A, R) = (1, 30) のとき
    # 10**9 を over するため
    for i in range(min(N-1, 30)):
        ans *= R
    if ans > 1_000_000_000:
        print('large')
    else:
        print(ans)