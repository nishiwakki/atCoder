# -*- coding: UTF-8 -*-

# 入力
N, M, Q = map(int, input().split())
# cnt[i]: 問題iを解いた人の数
cnt = [0] * (M+1)
# solved[i][j]: 参加者iが問題jを解いているときTrue
solved = [[False] * (M+1) for _ in range(N+1)]
# 答えを格納
ans = []
# クエリ処理
for q in range(Q):
    query = list(map(int, input().split()))
    # 1 n
    if len(query) == 2:
        n = query[1]
        val = 0
        for i in range(1, M+1):
            if solved[n][i]:
                val += N - cnt[i]
        ans.append(val)
    # 2 n m
    else:
        n, m = query[1], query[2]
        cnt[m] += 1
        solved[n][m] = True
# 出力
for i in ans:
    print(i)