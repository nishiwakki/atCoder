# -*- coding: UTF-8 -*-

from collections import Counter

# 入力
N, K = map(int, input().split())
S = [input() for _ in range(N)]
# Countオブジェクトを使って
# 出現回数の多い単語順に
C = list(Counter(S).most_common())
ans = C[K-1][0]
# 1番目を出力するなら
if K == 1:
    if not len(C) == 1:
        if C[K-1][1] == C[K][1]:
            ans = 'AMBIGUOUS'
# 最終番目を出力するなら
elif K == len(C):
    if C[K-1][1] == C[K-2][1]:
        ans = 'AMBIGUOUS'
# それ以外
else:
    if C[K-1][1] == C[K][1] \
    or C[K-1][1] == C[K-2][1]:
        ans = 'AMBIGUOUS'
# 出力
print(ans)