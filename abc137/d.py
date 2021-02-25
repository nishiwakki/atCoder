# -*- coding: UTF-8 -*-

import heapq

# 入力
N, M = map(int, input().split())
# バイトM件の入力
jobs = []
for _ in range(N):
    A, B = map(int, input().split())
    jobs.append((A, B))
# A日後が厳しい順にする(後ろに厳しいものを置く)
jobs.sort(reverse=True)
ans = 0
# 選択できるバイトをPriority_Queueで管理
can_jobs = []
heapq.heapify(can_jobs)
# M-1日から見ていく
for date in range(M-1, -1, -1):
    while jobs:
        need_date, reward = jobs.pop()
        if need_date > M - date:
            jobs.append((need_date, reward))
            break
        # 可能になるバイトをPQに突っ込む
        heapq.heappush(can_jobs, -reward)
    # そのdate日にできるバイトがあるなら
    # 一番報酬の良いバイトをやる
    if can_jobs:
        ans += -heapq.heappop(can_jobs)
# 出力
print(ans)