# -*- coding: UTF-8 -*-

# 入力
S = input()
# 各文字出現回数
chars = [0] * 26
for s in S:
    chars[ord(s)-97] += 1
# aから順に
for i in range(26):
    if not chars[i]:
        print(chr(i+97))
        exit()
# 全文字出現済みなので
print('None')