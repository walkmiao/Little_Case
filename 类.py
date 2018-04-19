#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 17:47
# @Author  : LCH
# @Site    : 
# @File    : 类.py
# @Software: PyCharm

class Student(object):
    # __slots__ = ['__age','__name']
    def __init__(self,age,name):
        if 0<age<100 and isinstance(name,str):
            self.__age=age
            self.__name=name
        else:
            raise ValueError('输入值不符合要求')
    @property
    def age(self):
        return self.__age
    def get_name(self):
        return self.__name
    @age.setter
    def age(self,age):
        if 0<age<100:
            self.__age=age



s=Student(90,'coco')
s.age=50
print(s.age)

