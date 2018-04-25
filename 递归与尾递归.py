#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 17:02
# @Author  : LCH
# @Site    : 
# @File    : 递归与尾递归.py
# @Software: PyCharm

#首先是一个常规的递归函数，比如计算n的阶乘
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5)) #相当于执行5*4*3*2*fact(1)

'''函数的调用是通过栈这种数据结构存储的，每当进入一个函数调用，栈就会增加一层栈帧。
每当函数返回则减少一层栈帧。由于栈的大小不是无限的，会出现栈溢出这种情况
'''
#print(fact(1000)) 执行这个函数就会报错

#解决这个问题可以通过尾递归优化，尾递归指函数返回的时候调用自身，而不是表达式
def fact2(n):
    return fact_iter(n,1)
def fact_iter(n,p):
    if n==1:
        return p
    return fact_iter(n-1,n*p)
print(fact2(1000))
