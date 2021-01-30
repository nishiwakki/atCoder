# -*- coding: UTF-8 -*-

# 入力
N = int(input())
A = list(map(int, input().split()))
# 長い棒順にソート(降順)
A.sort(reverse=True)
# 1つ前にチェックした辺の長さ
prev = A[0]
# 同じ長さが2本ある辺を記録
edge = []
for i in range(1, N):
    # 1つ前にチェックした辺と同じ長さ
    if prev == A[i]:
        # 同じ長さとして記録
        edge.append(A[i])
        # 0はどの辺とも一致しない
        prev = 0
    else:
        # 1つ前にチェックした辺として記録
        prev = A[i]
# 出力
# 同じ長さの辺が2セット以上あるとき
if len(edge) >= 2:
    print(edge[0] * edge[1])
else:
    print(0)