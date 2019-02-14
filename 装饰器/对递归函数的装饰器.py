#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 对递归函数的装饰器.py
# @Author: lch
# @Date  : 2018/12/12
# @Desc  :
import time
def clock(func):
    def wrap(*args):
        t0 = time.time()
        result = func(*args)
        param = ','.join([ repr(i) for i in args])
        elapsed = time.time()-t0
        print('[%0.8f]%s(%s) result:%r  run over...' %(elapsed, func.__name__, param, result))
        return result
    return wrap
@clock
def factorial(num):
    return 1 if num<2 else num*factorial(num-1)
f = factorial(6)