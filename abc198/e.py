# -*- coding: UTF-8 -*-

# 入力高速化
import sys
input = sys.stdin.readline

N = int(input())
C = [0] + list(map(int, input().split()))
# 隣接リスト作成
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)
# ans[v] = True
# 頂点v は よい頂点
ans = [False] * (N+1)
ans[1] = True
# DFSしている今の頂点
now = 1
# prv[v] = u
# 頂点v の根は 頂点u
prv = [0] * (N+1)
# col[i] = j
# 色i は j頂点分ある
col = [0] * (10**5+1)
col[C[1]] = 1
# DFS
while now:
    # 頂点now の隣接リストをcheck
    # 使用していないパスがあるなら先へ進む
    if adj[now]:
        next = adj[now].pop()
        if not col[C[next]]:
            ans[next] = True
        col[C[next]] += 1
        # 使用したパスの逆方向は削除
        adj[next].remove(now)
        # 根の頂点を記録
        prv[next] = now
        now = next
    # prvを参考に根の頂点へ戻る
    else:
        col[C[now]] -= 1
        if prv[now]:
            now = prv[now]
        else:
            # DFS終了
            now = 0
# 出力
for i in range(1, N+1):
    if ans[i]:
        print(i)