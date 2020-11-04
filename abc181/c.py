# -*- coding: UTF-8 -*-

# 同一直線上にあるか？
def check(x1, y1, x2, y2, x3, y3):
    # 全て同じx座標にある場合
    if x1 == x2 == x3:
        return True
    # 全て同じy座標にある場合
    if y1 == y2 == y3:
        return True
    dx1, dx2 = x2 - x1, x3 - x2
    dy1, dy2 = y2 - y1, y3 - y2
    if dx1 * dy2 == dx2 * dy1:
        return True
    return False

ans = False
N = int(input())
X, Y = [], []
# 入力受け取り
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
# 全パターンチェック
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if check(X[i], Y[i], X[j], Y[j], X[k], Y[k]):
                ans = True

# 解答出力
if ans:
    print('Yes')
else:
    print('No')
