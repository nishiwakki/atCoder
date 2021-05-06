# -*- coding: UTF-8 -*-

from itertools import permutations
import sys
input = sys.stdin.readline

# 入力
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
M = int(input())
X, Y = [0]*M, [0]*M
for i in range(M):
    X[i], Y[i] = map(int, input().split())
# 制約上, 10**4の答えがありうる
MAX = 10 ** 5
# 答えの初期値をセット
ans = MAX
# 順列全探索
for perm in permutations(range(N)):
    ok = True
    for i in range(M):
        runx, runy = perm[X[i]-1], perm[Y[i]-1]
        if abs(runx-runy) == 1:
            ok = False
            break
    if not ok:
        continue
    val = 0
    for who, run in enumerate(perm):
        val += A[who][run]
    ans = min(ans, val)
if ans == MAX:
    print(-1)
else:
    print(ans)