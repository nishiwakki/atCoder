# -*- coding: UTF-8 -*-

# 入力
X, Y, A, B = map(int, input().split())

# カコモンジムに通う
ans = 0
while X * A <= X + B and X * A < Y:
    X *= A
    ans += 1
# AtCoderジムに通う
ans += (Y - X - 1) // B
# 出力
print(ans)