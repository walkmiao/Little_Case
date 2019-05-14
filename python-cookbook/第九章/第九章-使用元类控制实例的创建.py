#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第九章-使用元类控制实例的创建.py
# @Author: lch
# @Date  : 2019/2/22
# @Desc  :
import weakref

class Cache(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._cache = weakref.WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if args not in cls._cache:
            obj = super().__call__(*args, **kwargs)
            cls._cache[args] = obj
        return cls._cache[args]


class Singleton(metaclass=Cache):
    def __init__(self,*args,**kw):
        pass


s1 = Singleton(1, 2)
s2 = Singleton(1, 2)
print(s1 is s2)
