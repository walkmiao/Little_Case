#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 20:25
# @Author  : LCH
# @Site    : 
# @File    : 类的属性.py
# @Software: PyCharm
class Test():
    def __init__(self, sex, name):
        self._sex = sex
        self.__name = name
class A(Test):
    pass

t= Test('male','lch')
print(t._sex)
a = A('female','ahot')
print(a._sex)
