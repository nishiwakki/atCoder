# -*- coding: UTF-8 -*-

# 入力最大値
MAX = 1_500_000
# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
# 出現回数リスト定義
cnt = [0] * (MAX+1)
# 0 ~ M-1の範囲でカウント
for i in range(M):
    cnt[A[i]] += 1
# 答え
ans = MAX
# 0 ~ M-1の範囲におけるmex算出 → ans
for i in range(MAX+1):
    if not cnt[i]:
        ans = i
        break
# 右にずれながら, M個の範囲から抜ける
# 整数に注目し, mexを確かめていく
for i in range(1, N-M+1):
    down, up = A[i-1], A[i+M-1]
    cnt[up] += 1
    cnt[down] -= 1
    if down < ans and cnt[down] == 0:
        ans = down
# 出力
print(ans)