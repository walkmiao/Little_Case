#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 19:44
# @Author  : LCH
# @Site    : 
# @File    : 定制类.py
# @Software: PyCharm
class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        if path == 'user':
            return lambda u : Chain('%s/%s/%s' % (self.path, path, u))
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__

c=Chain('lichunhui')
print(c.path)
print(c.user('animal'))

