# -*- coding: UTF-8 -*-

# 入力
S = input()
# 文字列(リスト)
stack = []
for s in S:
    if s == '0':
        stack.append(0)
    elif s == '1':
        stack.append(1)
    else:
        # 文字列が空でなければ
        if len(stack) > 0:
            stack.pop()
# 出力
for ans in stack:
    print(ans, end='')
print()