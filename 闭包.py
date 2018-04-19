#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 13:18
# @Author  : LCH
# @Site    : 
# @File    : 闭包.py
# @Software: PyCharm

def lazy_sum(*args):
    def sum():
        sum=0
        for i in args:
            sum=sum+i
        return sum
    return sum

print(lazy_sum(1,3,5)())

def lazy_test():
    fs=[]
    for i in range(1,4):
        def sum():
            return i*i
        fs.append(sum)
    return fs
f1,f2,f3=lazy_test()
print(f1(),f2(),f3())
