# -*- coding: UTF-8 -*-

from bisect import bisect_left

# 最長増加部分列
def lis(a):
    ret = [a[0]]
    for i in range(1, len(a)):
        if a[i] > ret[-1]:
            ret.append(a[i])
        else:
            idx = bisect_left(ret, a[i])
            ret[idx] = a[i]
    return ret

# 入力
N = int(input())
a = list(map(int, input().split()))
# 出力
print(len(lis(a)))