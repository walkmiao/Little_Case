#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 9:10
# @Author  : LCH
# @Site    : 
# @File    : 冒泡排序.py
# @Software: PyCharm
def maopao(temp):
    for i in range(len(temp)-1):
        for j in range(len(temp)-1-i):
            if temp[j]>temp[j+1]:
                temp[j+1],temp[j]=temp[j],temp[j+1]
    return temp
l=[101,52,18,29,35,37,20,99,76]
s=['a','c','z']
print(maopao(l))
print(max(s))
