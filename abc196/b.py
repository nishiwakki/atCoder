# -*- coding: UTF-8 -*-

X = input()
idx = X.find('.')
if idx == -1:
    print(X)
else:
    print(X[:idx])