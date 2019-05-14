#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第九章-为类和静态方法提供装饰器.py
# @Author: lch
# @Date  : 2019/2/22
# @Desc  :
from functools import wraps, partial


class staticmethod2:
    def __init__(self, func):
        wraps(func)(self)
        self._f = func

    def __call__(self, *args, **kwargs):
        pass

    def __get__(self, instance, owner):
        print(f'ins:{instance} owner:{owner}')
        return self._f



class classmethod2:
    def __init__(self, func):
        wraps(func)(self)
        self._f = func

    def __get__(self, instance, owner):
        return partial(self._f, owner)




class Generic:
    @staticmethod2
    def is_static(*args, **kw):
        print(f'staticmethod-->args:{args}, kw:{kw}')
    @classmethod2
    def is_class(cls, *args, **kw):
        print(f'classmethod--> cls:{cls} args:{args}, kw:{kw}')



g = Generic()
g.is_static(1,2,name='lch')
Generic.is_static(1,2,name='lch')
g.is_class(5,6,key='lichunhui')
Generic.is_class(7,8, name='hohoho')