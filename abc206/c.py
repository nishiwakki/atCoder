# -*- coding: UTF-8 -*-

from collections import Counter

N = int(input())
A = map(int, input().split())
C = Counter(A).most_common()
ans = 0
for a, cnt in C:
    N -= cnt
    ans += cnt * N
print(ans)