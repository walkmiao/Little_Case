#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 9:02
# @Author  : LCH
# @Site    : 
# @File    : 装饰器.py
# @Software: PyCharm
import datetime
import functools
import time

#不改变原函数的情况，通过装饰器增加打印函数调用前后花费的时间
def meric(f):
    @functools.wraps(f)
    def wrap(*args,**kw):
        start=time.time()
        tmp=f(*args, **kw)
        print('%s function cost %s ms' % (f.__name__, time.time() - start))
        return tmp
    return wrap
#编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def call(f):
    def wrap(*args,**kw):
        print('%s begin call..'%f.__name__)
        tmp=f(*args,**kw)
        print('%s end call...'%f.__name__)
        return tmp
    return wrap

@call
@meric
def f1(x,y):
    time.sleep(0.233)
    return x+y

@call
@meric
def f2(x,y,z):
    time.sleep(0.5666)
    return x*y*z
print(f1(10,10))
print(f2(3,4,5))
print(f1.__name__)








