# -*- coding: UTF-8 -*-

# 配列コピー(deepcopy)
from copy import deepcopy

# 配置列sに指定したタイプ操作を行なった後の配置を返す
def move(s, type):
    if type == 'A':
        for i in range(1, len(s)):
            if s[i] == '#':
                s[i-1] = '#'
    else:
        for i in range(len(s)-1, 0, -1):
            if s[i-1] == '#':
                s[i] = '#'
    return s

# 入力
N = int(input())
S = list(input())
# 答え
ans_a, ans_b = 50, 50
for a in range(50):
    for b in range(50):
        s = deepcopy(S)
        for i in range(a):
            move(s, 'A')
        for j in range(b):
            move(s, 'B')
        if s.count('#') == N:
            # 最小操作数なら更新
            if a + b < ans_a + ans_b:
                ans_a = a
                ans_b = b
# 出力
print(ans_a, ans_b)