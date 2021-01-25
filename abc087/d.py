# -*- coding: UTF-8 -*-

# 入力高速化
import sys
input = sys.stdin.readline

# 入力
N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for i in range(M):
    L, R, D = map(int, input().split())
    # 双方向についての隣接リスト
    adj[L].append((R, D))
    adj[R].append((L, -D))
# 矛盾ありならFalseとなる
ans = True
# 各頂点について(非連結があるため)
for v in range(1, N+1):
    # 頂点vについての隣接リストがあるなら
    if len(adj[v]) > 0:
        # DFSの準備
        # 頂点1~Nの位置について保持
        P = [-1] * (N+1)
        P[v] = 0
        st = [v]
        # スタックが空でないなら
        # (連結成分を全て調査可能)
        while len(st) > 0:
            top = st[-1]
            if len(adj[top]) > 0:
                next, dist = adj[top].pop()
                nextP = P[top] + dist
                # 頂点nextの位置情報がまだないなら
                if P[next] == -1:
                    P[next] = nextP
                else:
                    # 一致しないとき矛盾発生となる
                    if not P[next] == nextP:
                        ans = False
                st.append(next)
            else:
                st.pop()
# 出力
if ans:
    print('Yes')
else:
    print('No')