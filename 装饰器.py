#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 9:02
# @Author  : LCH
# @Site    : 
# @File    : 装饰器.py
# @Software: PyCharm
import datetime
import functools
def log(text=None):
    def wrap(func):
        @functools.wraps(func)
        def f0(*args,**kwargs):
            print('{0} is print'.format(text))
            return func(*args,**kwargs)
        return f0
    return wrap

@log()
def f1(num):
    print('the num is ',num)
f1(12)
@log()
def f2(num,age):
    print('the num is{0},the age is{1}'.format(num,age))

f2(10,99)



