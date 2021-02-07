# -*- coding: UTF-8 -*-

# 入力
N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for a in A:
    if not a == X:
        ans.append(a)
# 出力
print(*ans)