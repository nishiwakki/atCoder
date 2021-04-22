# -*- coding: UTF-8 -*-

# 入力
N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split())) + [L]
# 切れ目ごとの長さ
AA = [A[0]]
for i in range(1, N+1):
    AA.append(A[i] - A[i-1])

# 長さ leng 以上で切り分けていったとき
# K 回以内にようかんを分割できるか
def check(leng):
    # nl : 現在の長さ
    # cnt: 分割回数
    nl, cnt = 0, 0
    # 左端から貪欲に分割していく
    for a in AA:
        nl += a
        if nl >= leng:
            nl = 0
            cnt += 1
    # 分割した最後のようかんに注意
    if cnt > K:
        return True
    elif cnt == K:
        if nl >= leng:
            return True
        else:
            return False
    else:
        return False

# 決め打ち二分探索
l, r = 0, L
while l <= r:
    m = (l+r) // 2
    if check(m):
        l = m + 1
    else:
        r = m - 1
print(r)