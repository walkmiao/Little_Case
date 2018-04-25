#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 9:44
# @Author  : LCH
# @Site    : 
# @File    : 对象的实例变量.py
# @Software: PyCharm
class Student():

    def __init__(self,name,age):
        self.age=age
        self.name=name
s=Student('lch',20)
print(s.__dict__)