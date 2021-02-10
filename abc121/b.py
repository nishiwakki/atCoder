# -*- coding: UTF-8 -*-

# 入力
N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
# 正答コードの個数
ans = 0
for a in A:
    val = C
    for i, v in enumerate(a):
        val += B[i] * v
    if val > 0:
        ans += 1
# 出力
print(ans)