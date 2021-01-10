# -*- coding: UTF-8 -*-

# 入力高速化
import sys
input = sys.stdin.readline
# 入力
N = int(input())
vote = [0] * N
sumA, sumB = 0, 0
for i in range(N):
    a, b = map(int, input().split())
    sumA += a
    # 演説することで高橋派に入る票数
    # (青木票を2重カウントする)
    vote[i] = 2 * a + b
# 票数が多く入る町順に降順ソート
vote.sort(reverse=True)
# 演説する必要のある町の数
ans = 0
for v in vote:
    ans += 1
    sumB += v
    # 青木氏 < 高橋氏になったとき
    if sumA < sumB:
        break
# 出力
print(ans)