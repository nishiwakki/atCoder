# -*- coding: UTF-8 -*-

H, W = map(int, input().split())
if H == 1 or W == 1:
    print(max(H, W))
else:
    print(((H+1)//2) * ((W+1)//2))