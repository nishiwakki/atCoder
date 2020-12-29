# -*- coding: UTF-8 -*-

# 入力
N = int(input())
# 該当数をカウントアップ
ans = 0
for n in range(1, N+1):
    # 10進数
    ten = str(n)
    # 8進数('0o'は無視できる)
    eig = str(oct(n))
    # 10, 8進数表記に'7'が含まれていない場合
    if ten.count('7') == 0 and eig.count('7') == 0:
        ans += 1
# 出力
print(ans)