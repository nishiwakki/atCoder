# -*- coding: UTF-8 -*-

# 入力
w = input()
# 出現する文字をカウント
word = [0] * 26
for i in w:
    # 'a' = 97
    ii = ord(i) - 97
    word[ii] += 1
for i in word:
    # 偶数回の出現でなければ
    if not i % 2 == 0:
        print('No')
        exit()
print('Yes')