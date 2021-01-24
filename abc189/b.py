# -*- coding: UTF-8 -*-

# 入力
N, X = map(int, input().split())
V, P = [0] * N, [0] * N
for i in range(N):
    V[i], P[i] = map(int, input().split())
# 摂取したアルコール量 * 100
alc = 0
# 何杯目か(0なら'-1'の出力条件を満たす)
ans = 0
for i in range(N):
    alc += V[i] * P[i]
    if alc > X*100:
        ans = i + 1
        break
# 出力
if ans:
    print(ans)
else:
    print(-1)