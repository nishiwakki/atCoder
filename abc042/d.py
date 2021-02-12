# -*- coding: UTF-8 -*-

# MOD
MOD = 10**9 + 7
# 入力
H, W, A, B = map(int, input().split())
# 組み合わせ計算高速化(逆元)
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
for i in range(2, H+W+1):
    g1.append(g1[-1] * i % MOD)
    inverse.append(-inverse[MOD%i] * (MOD//i) % MOD)
    g2.append(g2[-1] * inverse[-1] % MOD)
# nCr を 定義
def comb(n, r, mod):
    if r < 0 or n < r:
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
# 答え
ans = 0
for w in range(B, W):
    h = H - A - 1
    val = comb(w+h, h, MOD) * comb(W-w+A-2, A-1, MOD) % MOD
    ans = (ans + val) % MOD
# 出力
print(ans)