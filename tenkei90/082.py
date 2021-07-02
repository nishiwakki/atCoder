# -*- coding: UTF-8 -*-

MOD = 10**9 + 7

# INPUT
L, R = map(int, input().split())
# L, Rの桁数をチェック
dig_L, dig_R = len(str(L)), len(str(R))
# 答え(文字の個数)を格納
ans = 0
# L, Rで桁数が異なる場合
while dig_L != dig_R:
    # Lが次の桁(10 ** dig_L)に上がるまでの文字の個数を計算
    cnt = (L+(10**dig_L-1)) * ((10**dig_L-1)-L+1) // 2
    ans = (ans + cnt*dig_L) % MOD
    # Lを次の桁の先頭数にする
    L = 10 ** dig_L
    dig_L += 1
cnt = (L+R) * (R-L+1) // 2
ans = (ans + cnt*dig_L) % MOD
# OUTPUT
print(ans)