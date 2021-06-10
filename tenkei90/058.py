# -*- coding: UTF-8 -*-

def calc(x):
    y = 0
    for i in str(x):
        y += int(i)
    return (x+y) % 100000

N, K = map(int, input().split())
vis = [False] * 100000
vis[N] = True
path = [N]
x = N
for k in range(K):
    next_x = calc(x)
    if vis[next_x]:
        break
    vis[next_x] = True
    path.append(next_x)
    x = next_x
if K < len(path):
    print(path[K])
else:
    idx = path.index(calc(x))
    roop = path[idx:]
    print(roop[(K-idx)%(len(path)-idx)])