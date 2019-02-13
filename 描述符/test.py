#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 16:25
# @Author  : LCH
# @Site    : 
# @File    : test.py
# @Software: PyCharm

#在对类中很多属性需要限制的地方--可以使用descriptor 描述符
#比如类中很多字段需要对值进行约束



class IntValidate:
    def __get__(self, ins, cls):
        if not hasattr(self, '_value'):
            raise Exception("please set the value first!")
        return self._value
    def __set__(self, ins, value):
        if isinstance(value, int) and 10<value<=100:
            self._value = value
            print('set value {} succ'.format(value))
        else:
            raise ValueError("don't set value <10 or >100")
    def __delete__(self, ins):
        del self._value


class Student:
    age = IntValidate()

s1 = Student()
# print(s1.age)
s1.age = 100
print(s1.age)
# del(s1.age)
# print(s1.age)

