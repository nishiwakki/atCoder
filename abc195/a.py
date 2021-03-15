# -*- coding: UTF-8 -*-

M, H = map(int, input().split())
# H % M == 0?
if not H % M:
    print('Yes')
else:
    print('No')