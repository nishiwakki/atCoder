# -*- coding: UTF-8 -*-

INF = 10**15
# 入力
N = int(input())
a, b, c = [0]*(N-1), [0]*(N-1), [0]*(N-1)
for i in range(N-1):
    a[i], b[i], c[i] = map(int, input().split())
Q, K = map(int, input().split())
x, y = [0]*Q, [0]*Q
for i in range(Q):
    x[i], y[i] = map(int, input().split())
adj = [[] for _ in range(N+1)]
# 隣接リスト作成
for i in range(N-1):
    adj[a[i]].append((b[i], c[i]))
    adj[b[i]].append((a[i], c[i]))
# dist[i]: 頂点Kと頂点iの最短経路の距離
dist = [INF] * (N+1)
dist[K] = 0
# スタック(DFS)
st = [K]
while len(st) > 0:
    top = st[-1]
    if len(adj[top]) > 0:
        next, sec_dist = adj[top].pop()
        if dist[next] == INF:
            dist[next] = dist[top] + sec_dist
            st.append(next)
    else:
        st.pop()
# 出力
for i in range(Q):
    # dist[x] + dist[y]が最短経路
    print(dist[x[i]] + dist[y[i]])