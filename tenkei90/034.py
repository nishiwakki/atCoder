# -*- coding: UTF-8 -*-

N, K = map(int, input().split())
A = list(map(int, input().split()))
dic = dict()
l, r, k = 0, 0, 0
ans = 0
while not l == N:
    if r == N:
        dic[A[l]] = dic[A[l]] - 1
        if not dic[A[l]]:
            k -= 1
        l += 1
    elif l == r:
        dic[A[r]] = 1
        k += 1
        r += 1
    else:
        if dic.get(A[r]):
            dic[A[r]] = dic[A[r]] + 1
            r += 1
        else:
            if k < K:
                dic[A[r]] = 1
                k += 1
                r += 1
            else:
                dic[A[l]] = dic[A[l]] - 1
                if not dic[A[l]]:
                    k -= 1
                l += 1
    ans = max(ans, r-l)
print(ans)