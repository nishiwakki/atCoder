# -*- coding: UTF-8 -*-

# 入力
N, L = map(int, input().split())
S = [input() for _ in range(N)]
S.sort()
# 出力
for s in S:
    print(s, end='')
print()