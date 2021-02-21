# -*- coding: UTF-8 -*-

# 入力
X, Y = map(int, input().split())
# Y != 0
if Y:
    # 丸め誤差考慮で桁多めに
    ans = '{:.10f}'.format(X/ Y)
    # 出力
    print(ans[:-8])
else:
    # 出力
    print('ERROR')