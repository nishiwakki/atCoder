# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
  ')' は '(' の数より多い分だけ
  文字列Sの最後に足せば良い

  しかし正しい括弧列にするために,
  '(' は ')' の数より多い分だけ...
  とはならないことに注意(入力例3)

  文字列Sを左からみていき,
  そこまでの ')' の数が '(' の数
  よりも多くなった時点で,
  文字列Sの先頭に'('を足す必要がある!!
~~~~~~~~~~~~~~~~~~~~'''

# 入力
N = int(input())
S = input()
# [ '(' の数] - [ ')' の数]
# 負になる場合は L に +1 する
cnt = 0
# 文字列Sの先頭に '(' を足す個数
L = 0
# 文字列Sの先頭から
for s in S:
    if s == '(':
        cnt += 1
    else:
        # '(' のストックがある場合
        if cnt:
            cnt -= 1
        # ない場合,
        # Sの先頭に '(' を足す必要あり
        else:
            L += 1
# ')' は最後に必要な分だけ足せば良い
R = cnt
# 出力
print('(' * L + S + ')' * R)