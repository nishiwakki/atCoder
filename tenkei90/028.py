import sys
input = sys.stdin.readline

LIM = 10**3 + 1
N = int(input())
G = [[0] * LIM for _ in range(LIM)]
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    G[lx][ly] += 1
    G[rx][ly] -= 1
    G[lx][ry] -= 1
    G[rx][ry] += 1
for x in range(LIM):
    for y in range(1, LIM):
        G[x][y] = G[x][y-1] + G[x][y]
for y in range(LIM):
    for x in range(1, LIM):
        G[x][y] = G[x-1][y] + G[x][y]
ans = [0] * (N+1)
for x in range(LIM):
    for y in range(LIM):
        ans[G[x][y]] += 1
for a in range(1, N+1):
    print(ans[a])