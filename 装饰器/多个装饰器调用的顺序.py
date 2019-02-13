#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : func_decorator.py
# @Author: lch
# @Date  : 2018/7/2
# @Desc  :

from functools import wraps
'''
多个装饰器调用的顺序是 调用从下而上 而执行是从上而下
'''
def decorator_a(func):
    print ('Get in decorator_a')
    # @wraps(func)
    def inner_a(*args, **kwargs):
        print ('Get in inner_a')
        print(func.__name__)

        return func(*args, **kwargs)
    return inner_a


def decorator_b(func):
    print ('Get in decorator_b')
    # @wraps(func)
    def inner_b(*args, **kwargs):
        print ('Get in inner_b')
        print(func.__name__)
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print ('Get in f')
    return x * 2
f(1)


