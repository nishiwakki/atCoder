# -*- coding: UTF-8 -*-

# 入力
N = int(input())
A = list(map(int, input().split()))

# GCD度が最大のときのkを保持
ans = 1
# 最大のときのGCD度
maxGCD = 0
# k=2から1000までGCD度を計算
for k in range(2, 1001):
    GCD = 0
    for a in A:
        if a % k == 0:
            GCD += 1
    # 更新する
    if GCD > maxGCD:
        ans = k
        maxGCD = GCD
# 出力
print(ans)