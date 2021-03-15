# -*- coding: UTF-8 -*-

A, B, Wkg = map(int, input().split())
Wg = Wkg * 1000
cnt = []
# みかんをi個選ぶとき
# A*i 以上, B*i 以下 の重さにできる
for i in range(1, 1000*1000+1):
    if A*i <= Wg <= B*i:
        cnt.append(i)
if cnt:
    print(cnt[0], cnt[-1])
else:
    print('UNSATISFIABLE')