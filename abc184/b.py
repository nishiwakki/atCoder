# -*- coding: UTF-8 -*-

# 入力
N, X = map(int, input().split())
S = input()
# 点数記録用：変数
ans = X
for s in S:
    if s == 'o':
        ans += 1
    else:
        ans = max(0, ans-1)
# 出力
print(ans)