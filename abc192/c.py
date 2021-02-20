# -*- coding: UTF-8 -*-

def g1(x):
    return int(''.join(sorted(list(str(x)), reverse=True)))

def g2(x):
    return int(''.join(sorted(list(str(x)))))

def f(x):
    return g1(x) - g2(x)

# 入力
N, K = map(int, input().split())
ans = N
for i in range(K):
    ans = f(ans)
# 出力
print(ans)