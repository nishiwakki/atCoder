# -*- coding: UTF-8 -*-

# 入力
N = int(input())
S = input()
ans, x = 0, 0
# 各文字について
for s in S:
    if s == 'I':
        x += 1
    else:
        x -= 1
    # 最大値を更新
    ans = max(ans, x)
# 出力
print(ans)