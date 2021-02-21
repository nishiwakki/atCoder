# -*- coding: UTF-8 -*-

# 入力
N, M, K = map(int, input().split())
s = [[0] * M for _ in range(N)]
for i in range(N):
    ss = input()
    for j in range(M):
        s[i][j] = int(ss[j])
ans = 0
# n = 1 ~ min(N, M) まで全調査
for n in range(1, min(N, M)+1):
    # st_i行目, st_j列目のマスから
    for st_i in range(N-n+1):
        for st_j in range(M-n+1):
            # 数字をカウント
            cnt = [0] * 10
            for i in range(st_i, st_i+n):
                for j in range(st_j, st_j+n):
                    cnt[s[i][j]] += 1
            # K回以下の数値変化で可能
            if n ** 2 - max(cnt) <= K:
                ans = n
# 出力
print(ans)