# -*- coding: UTF-8 -*-

from operator import itemgetter

N, M, Q = map(int, input().split())
items = []
for i in range(N):
    W, V = map(int, input().split())
    items.append((W, V))
# W(重さ)が大きい順, V(価値)が大きい順でソート
# → 価値が大きい順(同価値の場合重さが大きい方が前)
items.sort(key=itemgetter(0), reverse=True)
items.sort(key=itemgetter(1), reverse=True)
X = list(map(int, input().split()))
for q in range(Q):
    L, R = map(int, input().split())
    # 使える箱だけ選出
    x = X[:L-1] + X[R:]
    x.sort()
    ans = 0
    used = [False] * N
    # 小さい箱から順に
    for xi in x:
        # 価値の大きい荷物から順に
        for i in range(N):
            w, v = items[i][0], items[i][1]
            # 箱に入れられる かつ まだ残っている荷物
            if w <= xi and not used[i]:
                ans += v
                used[i] = True
                break
    print(ans)