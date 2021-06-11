# -*- coding: UTF-8 -*-

from itertools import product

H, W = map(int, input().split())
P = [list(map(int, input().split())) for h in range(H)]
ans = 0
for p in product(range(2), repeat=H):
    cnt = [0] * (H*W+1)
    sump = sum(p)
    for w in range(W):
        num = 0
        flg = True
        for h in range(H):
            if p[h]:
                if not num:
                    num = P[h][w]
                elif not num == P[h][w]:
                    flg = False
                    break
        if flg and num:
            cnt[num] += sump
    ans = max(ans, max(cnt))
print(ans)