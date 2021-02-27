# -*- coding: UTF-8 -*-

'''~~~~~~~~~~~~~~~~~~~~
建物A → 建物B の移動は必ずするため,
最低でも x 分かかる.
この移動によって,
- 同階への移動 [EX] (a, b) = (5, 5)
- 1つ下の階への移動 [EX] (a, b) = (5, 4)
は目的を達成することができる.
ここからは下記2つで場合分けをする.
1. a < b
    1階分を上がる方法として,
    - A→B→A で 2x 分
    - A→B   で  y 分
    の2種類があるので, 早い方を使用すれば良い.
2. a < b 以外
    1 と同様であるが, 必ず行う
    建物A → 建物B の移動によって,
    1階分をスキップして考えることができる点に注意.
~~~~~~~~~~~~~~~~~~~~'''

# 入力
a, b, x, y = map(int, input().split())
# 場合わけ
if a == b or a-1 == b:
    print(x)
elif a < b:
    if 2*x < y:
        print(x + 2 * x * (b-a))
    else:
        print(x + y * (b-a))
else:
    if 2*x < y:
        print(x + 2 * x * (a-b-1))
    else:
        print(x + y * (a-b-1))