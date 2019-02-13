#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 不执行装饰函数的装饰器.py
# @Author: lch
# @Date  : 2018/8/22
# @Desc  :
def log(func):
    def decorator(*args,**kw):
        print('准备执行%s'%func.__name__)
        return func
    return decorator
@log
def print_now():
    print('22222')
f = print_now()
print(f())