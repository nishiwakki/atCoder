# -*- coding: UTF-8 -*-

'''~~~~~~~~~~
[ASCII Code]
A: 65
Z: 90
a: 97
z: 122
~~~~~~~~~~'''

# 入力
S = input()
ans = True
for i in range(len(S)):
    # 奇数番目
    if (i+1) % 2:
        # 大文字なら読みやすい
        if ord(S[i]) < 91:
            ans = False
    # 偶数番目
    else:
        # 小文字なら読みやすい
        if ord(S[i]) > 96:
            ans = False
# 出力
if ans:
    print('Yes')
else:
    print('No')