#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 元类的使用.py
# @Author: lch
# @Date  : 2018/10/11
# @Desc  :
'''
简单回顾下元类的使用
'''

class IsMetalclass(type):
    def __new__(cls, cls_name, base, attr):
        print('will generator {}({})'.format(cls_name,base))
        attr['add'] = lambda self, value:self.append(value)
        base_cls = super(IsMetalclass, cls)
        print('base_cls:{}'.format(base_cls))
        return super(IsMetalclass, cls).__new__(cls, cls_name, base, attr)

class Model(list, metaclass=IsMetalclass):
    def __init__(self):
        print('cls:{}'.format(self.__class__.__name__))

m = Model()
m.add(1)
print(m)
