# -*- coding: UTF-8 -*-

import itertools # bit全探索で使用

# 入力
N = input()
# 入力の桁数取得
length = len(N)
# 出力値はlength-1未満 or -1 となる
ans = length - 1
# Trueのとき3の倍数がつくれない
cannotDiv = True
# [0, 1]でlength桁分のbit状態を取得
all_state = list(itertools.product([0, 1], repeat=length))
for state in all_state:
    # 残す桁の総和
    sumVal = 0
    # 削除する桁数
    deldig = 0
    # 各桁をチェック(length桁分)
    for i in range(length):
        # i桁目のstateが1(桁を残す)の場合
        if state[i] == 1:
            sumVal += int(N[i])
        # state=0は桁削除
        else:
            deldig += 1
    # 総和が3で割り切れるか(3の倍数か)?
    # かつ、全て桁を消すstateでないか?
    if sumVal % 3 == 0 and sumVal > 0:
        cannotDiv = False
        # 小さい削除桁数で更新していく
        ans = min(ans, deldig)
# 出力
# 3の倍数がつくれるか?
if not cannotDiv:
    print(ans)
else:
    print(-1)