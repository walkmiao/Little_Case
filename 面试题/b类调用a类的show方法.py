#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : b类调用a类的show方法.py
# @Author: lch
# @Date  : 2018/10/15
# @Desc  :

class A():
    def show(self):
        print('i am A class')

class B(A):
    def show(self):
        print('i am B class')

t = B()
t.__class__=A
t.show()
'''
如何调用A类的show
'''
