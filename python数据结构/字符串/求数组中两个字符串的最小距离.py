#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 求数组中两个字符串的最小距离.py
# @Author: lch
# @Date  : 2018/6/5
# @Desc  :
'''
给定一个数组 strs，其中的数据都是字符串，给定两个字符串 str1，str2。如果这两个字符串都在 strs数组中，
就返回它们之间的最小距离；如果其中任何一个不在里面，则返回 -1；如果两个字符串相等，则返回 0。
例如：给定[‘*’,’3’,’*’,’5’,’10’,’9’,’7’,’1’,’*’]，再给定两个字符串’* ‘和’9’，通过函数求得返回值 3。
'''
def min_distance(arr,str1, str2):
    d = dict()
    min = len(arr)
    if str1 not in arr or str2 not in arr:
        return -1
    elif str1 == str2:
        return 0
    else:
        for k, v in enumerate(arr):
            if str1 == v:
                d.setdefault(str1,[]).append(k)
            if str2 == v:
                d.setdefault(str2,[]).append(k)
        for i in d[str1]:
            for j in d[str2]:
                dis = abs(i - j)
                if dis < min:
                    min = dis
        return min




arr = ['*', '3','*','5','10','9','7','1','*']
print(min_distance(arr,'*','9'))