# -*- coding: UTF-8 -*-

# 入力
S, P = map(int, input().split())
# 0 ~ √P まで
for N in range(int(P**0.5)+1):
    # 条件を満たすならYes
    if N * (S-N) == P:
        print('Yes')
        exit()
print('No')