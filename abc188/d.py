# -*- coding: UTF-8 -*-

'''----------------------------------------------
[Ex] N=3, C=10
1 8 5
3 6 7
4 9 8
servicesにimos法の要領で追加
[[time1, cost_change1],
 [time2, cost_change2],
 ...
]
timeの差分を取り、cost_changeによる支払い料と乗算する。
cost_change > Cのとき、Cで計算することを忘れずに
----------------------------------------------'''

# 入力
N, C = map(int, input().split())
# サービスの内容を格納
services = []
for i in range(N):
    a, b, c = map(int, input().split())
    # サービス開始による支払いを追加
    services.append([a, c])
    # サービス終了による支払いを削除
    services.append([b+1, -c])
# timeで昇順ソート
services.sort()
# 合計金額
ans = 0
last_time = services[0][0]
cost_change = 0
for time, change in services:
    # 使用サービスの値段がC(snukePrime)を超えたとき
    # snukePrimeの方が安くなる
    if cost_change > C:
        ans += C * (time - last_time)
    # 各サービスを使用する
    else:
        ans += cost_change * (time - last_time)
    cost_change += change
    last_time = time
# 出力
print(ans)