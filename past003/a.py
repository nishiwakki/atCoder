# -*- coding: UTF-8 -*-

# 入力
s = input()
t = input()
# 出力
if s == t:
    print('same')
# 大文字に揃える
elif s.upper() == t.upper():
    print('case-insensitive')
else:
    print('different')