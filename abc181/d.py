# -*- coding: UTF-8 -*-

# 入力
S = input()

# 1桁の時
if len(S) == 1:
    # 8のみYes
    if int(S) == 8:
        print('Yes')
    else:
        print('No')
# 2桁の時
elif len(S) == 2:
    # 逆順num2もチェック対象
    num1 = int(S[0] + S[1])
    num2 = int(S[1] + S[0])
    # 8で割り切れるか?
    if num1 % 8 == 0 or num2 % 8 == 0:
        print('Yes')
    else:
        print('No')
# 3桁以上の時
else:
    # TrueになればYes
    flag = False
    # Sの数字の出現回数を保持
    numCount = [0] * 10
    # 使用できる数字をリストにしておく
    numUse = []
    for i in S:
        # 下3桁のみチェックするため、同数字4つ以上は不要
        if numCount[int(i)] < 3:
            numUse.append(i)
            numCount[int(i)] += 1
    numUselen = len(numUse)
    for i in range(numUselen):
        for j in range(numUselen):
            for k in range(numUselen):
                # 同じindexでの数字形成はNG
                if i == j or j == k or k == i:
                    continue
                if int(numUse[i] + numUse[j] + numUse[k]) % 8 == 0:
                    flag = True
    if flag:
        print('Yes')
    else:
        print('No')
