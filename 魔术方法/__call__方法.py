#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 20:54
# @Author  : lch
# @File    : __call__方法.py
'''
__call__方法使用
'''
import functools
class CacheProperty():
    _cache = {}
    def __call__(self, f):
        @property
        @functools.wraps(f)
        def wrapped(self):
            print(self)
            k='%s:%s'%(id(self),f.__name__)
            print('k:%s'%k)
            v = CacheProperty._cache.get(k)
            if not v:
                v = f(self)
                print('v:%s'%v)
                CacheProperty._cache[k]=v
            return v
        return wrapped

cached_property=CacheProperty()
print(callable(CacheProperty))
print(callable(cached_property))
class DB():
    def __init__(self):
        print(self)
    def create_conn(self):
        return 'create_conn result'
    @cached_property
    def conn(self):
        return self.create_conn()

db=DB()
db.conn

