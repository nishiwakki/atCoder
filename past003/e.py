# -*- coding: UTF-8 -*-

# 入力
N, M, Q = map(int, input().split())
# 隣接リスト作成
adj = [[] for i in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
c = [0] + list(map(int, input().split()))
# 答え
ans = []
# クエリ処理
for q in range(Q):
    query = list(map(int, input().split()))
    # 1 x
    if len(query) == 2:
        x = query[1]
        ans.append(c[x])
        for a in adj[x]:
            c[a] = c[x]
    # 2 x y
    else:
        x, y = query[1], query[2]
        ans.append(c[x])
        c[x] = y
# 出力
for a in ans:
    print(a)