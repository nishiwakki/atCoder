# -*- coding: UTF-8 -*-

# 入力
K, S = map(int, input().split())
# 条件を満たす組の数
ans = 0
# 0 <= X <= K
for X in range(K+1):
    # 0 <= Y <= K
    for Y in range(K+1):
        Z = S - X - Y
        if 0 <= Z <= K:
            ans += 1
# 出力
print(ans)