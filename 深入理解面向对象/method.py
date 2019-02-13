#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : method.py
# @Author: lch
# @Date  : 2018/9/27
# @Desc  :
def foo(x):
    print ("executing foo(%s)"%(x))

class A(object):
    def foo(self,x):
        print ("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print ("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)

a=A()
A.foo(a,'t1')
a.foo('t2')
a.class_foo('t3')
print(a.foo)