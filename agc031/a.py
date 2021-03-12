# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
出現する文字について,どの文字を使うか
(出現回数)+1[通り] の選択肢がある.
Sに出てくる文字全てについて,
上記を全てかけ合わせれば良い.
~~~~~~~~~~~~~~~~~~~~'''

from collections import defaultdict

MOD = 10 ** 9 + 7
N = int(input())
S = input()
dd = defaultdict(int)
for s in S:
    dd[s] += 1
ans = 1
for d in dd.values():
    ans = ans * (d+1) % MOD
ans = (ans-1) % MOD
print(ans)