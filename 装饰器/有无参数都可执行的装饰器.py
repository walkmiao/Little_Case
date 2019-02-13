#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 有无参数都可执行的装饰器.py
# @Author: lch
# @Date  : 2018/7/2
# @Desc  :
from functools import wraps


def log(para):
    def decorator(func=para):
        text = 'call' if func == para else para

        @wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator() if callable(para) else decorator


@log('excute')
def show():
    print('2018-09-06')


show()