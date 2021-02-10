# -*- coding: UTF-8 -*-

# 入力
N, M = map(int, input().split())
# Aが安価なものから栄養ドリンクを買うと最安値
AB = sorted([tuple(map(int, input().split())) for _ in range(N)])
ans, cnt = 0, 0
for i in range(N):
    a, b = AB[i]
    ans += a * min(b, M-cnt)
    cnt += b
    if cnt >= M:
        break
# 出力
print(ans)