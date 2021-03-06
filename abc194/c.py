# -*- coding: UTF-8 -*-

# num[0]   = -200
# num[1]   = -199
# num[200] = 0
# num[399] = 199
# num[400] = 200

# 入力
N = int(input())
A = list(map(int, input().split()))
# 答え
ans = 0
# num 作成
num = [0] * 401
for a in A:
    num[a+200] += 1
# numごとに
for i in range(401):
    for j in range(i+1, 401):
        a, b = i-200, j-200
        val = abs(a-b) ** 2
        ans += (num[i] * num[j]) * val
# 出力
print(ans)