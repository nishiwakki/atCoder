# -*- coding: UTF-8 -*-

# 入力
A, B = map(int, input().split())
# 出力
print(max(A+B, A-B, A*B))