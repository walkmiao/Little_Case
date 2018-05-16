#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : super用法.py
# @Author: lch
# @Date  : 2018/5/11
# @Desc  :

class Base():
    def __init__(self):
        print('enter Base')
        print('leave Base')

class A(Base):
    def __init__(self):
        print('enter A')
        super(A,self).__init__()
        print('leave A')

class B(Base):
    def __init__(self):
        print('enter B')
        super(B,self).__init__()
        print('leave B')

class C(A,B,Base):
    def __init__(self):
        print('enter C')
        super(C,self).__init__()
        print('leave C')

#super不是一个方法而是一个类,super的实现看下面的函数，获取inst的类的MRO列表。查找cls在MRO列表的位置返回下一个位置的类
# def super(cls,inst):
#     mro=inst.__class__.mro()
#     return mro[mro.index(cls)+1]


#查看下面的输出，super和父类没有实质性的关联，而是像上面的super函数的原理
print(C.mro())
c=C()
