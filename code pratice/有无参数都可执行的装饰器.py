#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 有无参数都可执行的装饰器.py
# @Author: lch
# @Date  : 2018/10/12
# @Desc  :
import time


def log(para):
    def wrapper(func=para):
        def decorator():
            if func==para:
                print('装饰器不带参数')
                return func()
            else:
                print("装饰器带参数:%s" % para)
                return func()
        return decorator
    return wrapper() if callable(para) else wrapper


@log('dd')
def simple():
    print('time is {}'.format(time.ctime()))

simple()