# -*- coding: UTF-8 -*-

# 入力
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

# 0手目：同じマスか
if r1 == r2 and c1 == c2:
    ans = 0
# 1手目：a+b = c+d 
elif r1 + c1 == r2 + c2:
    ans = 1
# 1手目：a-b = c-d
elif r1 - c1 == r2 - c2:
    ans = 1
# 1手目：|a-c| + |b-d| <= 3
elif abs(r1-r2) + abs(c1-c2) <= 3:
    ans = 1
# 2手目：パリティが等しい
elif ((r1 + c1) % 2) == ((r2 + c2) % 2):
    ans = 2
# 2手目：|a-c| + |b-d| <= 6
elif abs(r1-r2) + abs(c1-c2) <= 6:
    ans = 2
# 2手目：|(a+b) - (c+d)| <= 3
elif abs((r1 + c1) - (r2 + c2)) <= 3:
    ans = 2
# 2手目：|(a-b) - (c-d)| <= 3
elif abs((r1 - c1) - (r2 - c2)) <= 3:
    ans = 2
# それ以外は全て3手
else:
    ans = 3

# 出力
print(ans)