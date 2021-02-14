# -*- coding: UTF-8 -*-

# 入力
s = input()
# 文字列sの長さ
l = len(s)
# 文字列sを左から
for i in range(l-1):
    # index out of range 回避
    if not i+2 >= l:
        # XYX は unbalance
        if s[i] == s[i+2]:
            print(i+1, i+3)
            exit()
    # XX は unbalance
    if s[i] == s[i+1]:
        print(i+1, i+2)
        exit()
# unbalance がない
print(-1, -1)