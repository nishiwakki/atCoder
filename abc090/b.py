# -*- coding: UTF-8 -*-

# 入力
A, B = map(int, input().split())
# 回文数の個数
ans = 0
# A以上B以下に対して
for i in range(A, B+1):
    # 回文チェック
    s = list(str(i))
    ss = list(reversed(s))
    # 回文なら
    if s == ss:
        ans += 1
# 出力
print(ans)