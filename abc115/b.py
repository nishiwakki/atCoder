# -*- coding: UTF-8 -*-

# 入力
N = int(input())
p = [int(input()) for _ in range(N)]
# 降順ソート
p.sort(reverse=True)
# 1番目が最も定価が高いため半額で買う
ans = p[0] // 2
# それ以外は定価で買う
ans += sum(p[1:])
# 出力
print(ans)