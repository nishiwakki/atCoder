# -*- coding: UTF-8 -*-

# 入力
N = int(input())
# アナグラムの個数
ans = 0
# 辞書で管理
dic = dict()
# 各文字列sについて
for i in range(N):
    s = list(input())
    s.sort()
    ss = ''.join(s)
    if ss in dic:
        ans += dic[ss]
        dic[ss] = dic[ss] + 1
    else:
        dic[ss] = 1
# 出力
print(ans)