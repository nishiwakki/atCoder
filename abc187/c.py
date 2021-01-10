# -*- coding: UTF-8 -*-

'''------------------------
・不満な文字列とは
  'a'及び'!a'のような文字列が
  Sに両方含まれているとき
------------------------'''

# 入力
n = int(input())
S = []
for i in range(n):
    s = input()
    if s[0] == '!':
        # '!'を後ろへ
        S.append(s[1:] + '!')
    else:
        S.append(s)
# ソート
S.sort()
# リストの隣接をチェック
for i in range(n-1):
    if S[i]+'!' == S[i+1]:
        # 1つ示して終了
        print(S[i])
        exit()
# 不満な文字列がないとき出力
print('satisfiable')