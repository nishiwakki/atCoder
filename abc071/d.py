# -*- coding: UTF-8 -*-

MOD = 10**9 + 7
# 入力
N = int(input())
S1 = input()
S2 = input()
# N=1のとき別処理
if N == 1:
    print(3)
    exit()
# 塗り方をカウント
ans = 0
# 1*2を縦に敷き詰めるとき
# 次のチェック列は無視する
is_next = True
for i in range(N):
    # 前列で1*2を敷き詰めているとき
    if not is_next:
        is_next = True
        continue
    # 最終列のチェックは必ず2*1が敷き詰められる
    if i == N-1:
        if S1[i-1] == S2[i-1]:
            ans = ans * 2 % MOD
        continue
    # 1*2を敷き詰めるとき
    if S1[i] == S1[i+1]:
        is_next = False
        # i = 0 のとき
        if not ans:
            ans = 6
        else:
            # 前ペアが2*1のとき
            if S1[i-1] == S2[i-1]:
                ans = ans * 2 % MOD
            # 前ペアが1*2のとき
            else:
                ans = ans * 3 % MOD
    # 2*1を敷き詰めるとき
    else:
        # i = 0 のとき
        if not ans:
            ans = 3
        else:
            # 前ペアが2*1のとき
            if S1[i-1] == S2[i-1]:
                ans = ans * 2 % MOD
            '''
            # 前ペアが1*2のとき
            else:
                ans = ans * 1 % MOD
            '''
# 出力
print(ans)