#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 11:07
# @Author  : LCH
# @Site    : 
# @File    : 返回函数.py
# @Software: PyCharm

#把函数作为返回值返回
def lazy_sum(*args):
    def add():
        sum=0
        for i in args:
            sum=sum+i
        return sum
    return add

f=lazy_sum(*range(1,10))
print(f)
print(f())
l=[1,3,4]
