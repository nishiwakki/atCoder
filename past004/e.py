# -*- coding: UTF-8 -*-

from itertools import permutations

# 入力
N = int(input())
S = list(input())
# 最初は None でセット
ans = None
# 順列全探索
for T in permutations(S):
    T = list(T)
    # T と S が同じ?
    if T == S:
        continue
    # T を 逆順
    T.reverse()
    # 逆順 T と S が同じ?
    if T == S:
        continue
    # 全ての条件を満たす
    ans = ''.join(T)
# 出力
print(ans)