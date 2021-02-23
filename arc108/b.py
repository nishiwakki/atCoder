# -*- coding: UTF-8 -*-

# 入力
N = int(input())
S = list(input())
T = []
for s in S:
    T.append(s)
    if len(T) < 3:
        continue
    # Tの末尾3文字が'fox'なら取り出し
    if ''.join(T[len(T)-3:len(T)]) == 'fox':
        [T.pop() for _ in range(3)]
# 出力
print(len(T))