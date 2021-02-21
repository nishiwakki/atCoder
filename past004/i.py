# -*- coding: UTF-8 -*-

# 入力
N = int(input())
a = list(map(int, input().split()))
X, Y = 0, sum(a)
# 円環は扱いづらいので a を2つ並べて考える
a = a * 2
ans = Y
l, r = -1, -1
while not (l == 2*N-1 and r == 2*N-1):
    # 食べるピースを増やすしかない
    if l == r:
        r += 1
        X += a[r]
        Y -= a[r]
    # 食べるピースを減らすしかない
    elif r == 2*N-1:
        l += 1
        X -= a[l]
        Y += a[l]
    else:
        # 最小値 0 未満の答えはないのでbreak
        if X == Y:
            break
        # 食べるピースを増やす
        elif X < Y:
            r += 1
            X += a[r]
            Y -= a[r]
        # 食べるピースを減らす
        else:
            l += 1
            X -= a[l]
            Y += a[l]
    # |X-Y| の最小値を更新
    ans = min(ans, abs(X-Y))
# 出力
print(ans)