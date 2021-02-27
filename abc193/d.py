# -*- coding: UTF-8 -*-

# 入力
K = int(input())
S = input()[:-1]
T = input()[:-1]
# 全カードの残り枚数
# cardA[3]: 3のカードの枚数
cardA = [K] * 10
# 高橋くんのカード枚数
cardS = [0] * 10
for i in S:
    cardS[int(i)] += 1
    cardA[int(i)] -= 1
# 高橋くんの予測点数
# scoreS[3]: 裏向きカードが3の場合の点数
scoreS = [0] * 10
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            scoreS[i] += j * (10 ** (cardS[j]+1))
        else:
            scoreS[i] += j * (10 ** cardS[j])
# 青木くんのカード枚数
cardT = [0] * 10
for i in T:
    cardT[int(i)] += 1
    cardA[int(i)] -= 1
# 青木くんの予測点数
scoreT = [0] * 10
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            scoreT[i] += j * (10 ** (cardT[j]+1))
        else:
            scoreT[i] += j * (10 ** cardT[j])
# 答えの確率
ans = 0
# 残り枚数
remain = K * 9 - 8
# 高橋くんの裏のカードが 1~9
for s in range(1, 10):
    # 青木くんの裏のカードが 1~9
    for t in range(1, 10):
        # 高橋くんのスコアの方が高いなら
        if scoreS[s] > scoreT[t]:
            # 同じ数字のカードを引く場合は要注意
            if s == t:
                ans += (cardA[s] / remain) * ((cardA[t]-1) / (remain-1))
            else:
                ans += (cardA[s] / remain) * ((cardA[t]) / (remain-1))
# 出力
print(ans)