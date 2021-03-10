# -*- coding: UTF-8 -*-

# 入力
B, C = map(int, input().split())
# -abs(B) <= x <= abs(B) の整数
# 総数は0を含む abs(B) * 2 + 1
ans = 1 + min(C, abs(B)*2)
# 上の範囲外で整数を増やすとき,
# B<=0なら, C=2から1ずつ増加
# B> 0なら, C=3から1ずつ増加
if B <= 0:
    ans += C-1
else:
    ans += max(0, C-2)
# 出力
print(ans)