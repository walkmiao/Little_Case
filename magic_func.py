#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : magic_func.py
# @Author: lch
# @Date  : 2018/5/11
# @Desc  :
'''
python的魔术方法有很多，比如init，new，str，repr等，下面就来实地测试下这些魔术方法的具体用法
'''

# class Student():
#     #init用来作类的实例化
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     #str用来改变实例的显示方式
#     def __str__(self):
#         return 'Student instance <name=%s,age=%d>'%(self.name,self.age)
#
# s=Student('lulu',18)
# print(s)

class A(object):
    def __new__(cls, *args, **kwargs):
        for i in args:
            print('thi is %s.__new__ func and value is %d'%(cls,i))
        return super(A,cls)

a=A(*[100])
print(a)


class UpperStr(str):
    def __new__(cls, string=""):
        return str.__new__(cls, string.upper())


hello = UpperStr("hello world!")
print(hello)
