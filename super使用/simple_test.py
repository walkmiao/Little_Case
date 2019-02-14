#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 15:24
# @Author  : LCH
# @Site    : 
# @File    : simple_test.py
# @Software: PyCharm


class Base:
    def __init__(self, name):
        self.name = name

    def func(self):
        print(' i am func')

class Demo(Base):
    pass

print(type(Demo))


b = Base('hello')
print(b.func)
print(Base.func)
print(Base.__dict__['func'].__get__(b, Base) == b.func)
print(type(Base.__dict__))