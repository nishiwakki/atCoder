# -*- coding: UTF-8 -*-

# 入力
N = int(input())
a = list(map(int, input().split()))
# 答え, 区間和
ans, val = 0, 0
# 尺取り
l, r = 0, 0
while not l == N:
    if r == N:
        val -= a[l]
        l += 1
    elif l == r:
        val += a[r]
        r += 1
    else:
        if val >= N:
            val -= a[l]
            l += 1
        else:
            val += a[r]
            r += 1
    if val == N:
        ans += 1
# 出力
print(ans)