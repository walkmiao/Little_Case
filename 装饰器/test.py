#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 21:51
# @Author  : lch
# @File    : decorator1.py
import time,functools
'''
函数也是一个对象，python中皆是对象
'''
# def sum_1(a,b):
#     return a+b
# print(sum_1(1,2),sum_1)
# sum_1=1 #当sum_1指向为一个int对象后，已经不再是之前的函数了
# print(sum_1.__class__)
# # sum_1(1,2) 这里就会报错

#闭包
def f1(a):
    def f2(b):
        if a>=b:
            print('{} >= {}'.format(a,b))
        print('{} < {}'.format(a,b))
    return f2

f=f1(10)
f(11)

#装饰器,装饰器其实就是闭包的一个语法糖.为了在不改变原函数的情况下增添其他功能
def a(fn):
    @functools.wraps(fn) #如果不添加这句 函数的名称就会变成b,因为现在的f=b了。在某些依赖函数签名的场景里，需要保证原函数名的不变
    def b(*args):
        print('call %s at %s'%(fn.__name__,time.ctime()))
        return fn(*args)
    return b
@a #这里相当于 f=a(f)
def f(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(f(1,2))
print(f.__name__)

#带有参数的装饰器,则要构造三层嵌套 第二层中传入函数
def a(text):
    def b(fn):
        def c(*args):
            print('text is %s'%text)
            return fn(*args)
        return c
    return b
@a('测试执行')
def f(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(f(1,2,3,4,5))