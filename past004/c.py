# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
下記のように考えると,
i = 1, N や j = 1, M
でのindexErrorを防げる.
3 4
#.##
..#.
#...
 ↓
......
.#.##.
...#..
.#....
......
~~~~~~~~~~~~~~~~~~~~'''

# 入力
N, M = map(int, input().split())
s = []
s.append('.' * (M+2))
for i in range(N):
    s.append('.' + input() + '.')
s.append('.' * (M+2))
# 答えを保持
ans = [[0] * M for _ in range(N)]
# 各マスについて
for i in range(1, N+1):
    for j in range(1, M+1):
        grid = [s[i-1][j-1], s[i-1][j], s[i-1][j+1],
                s[i  ][j-1], s[i  ][j], s[i  ][j+1], 
                s[i+1][j-1], s[i+1][j], s[i+1][j+1]]
        ans[i-1][j-1] = grid.count('#')
# 出力
for i in ans:
    for j in i:
        print(j, end='')
    print()