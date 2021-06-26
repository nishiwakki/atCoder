# -*- coding: UTF-8 -*-

N = int(input())
A = list(map(int, input().split()))
SUM = sum(A)
# 制約下より不可
if SUM % 10:
    print('No')
    exit()
# 目標の面積
psum = SUM // 10
# 隣接を考慮
A = A + A
# 尺取り法
l, r = -1, 0
nsum = A[0]
while not (l == 2*N-1 and r == 2*N-1):
    moveR = True
    if r == 2*N-1:
        moveR = False
    elif l == r:
        pass
    else:
        if nsum == psum:
            pass
        elif nsum > psum:
            moveR = False
        else:
            pass
    # check
    if nsum == psum:
        print('Yes')
        exit()
    # 右に動かすか?
    if moveR:
        r += 1
        nsum += A[r]
    else:
        l += 1
        nsum -= A[l]
print('No')