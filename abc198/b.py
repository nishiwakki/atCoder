# -*- coding: UTF-8 -*-

# 回文判定
def is_palindrome(s):
    l = len(s)
    for i in range(0, l, 2):
        if not s[i] == s[l-i-1]:
            return False
    return True

N = input()
for i in range(10):
    if is_palindrome('0' * i + N):
        print('Yes')
        exit()
print('No')