# -*- coding: UTF-8 -*-

# 入力
K = int(input())
# 該当数を数え上げ
ans = 0
# A, Bを全探索
for A in range(1, K+1):
    for B in range(1, K+1):
        AB = A * B
        # Cは1未満になるためbreak
        if AB > K:
            break
        # AB=3, K=16 なら
        # C=1,2,3,4,5 となる
        ans += K // AB
# 出力
print(ans)