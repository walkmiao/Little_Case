#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 17:19
# @Author  : LCH
# @Site    : 
# @File    : stackoverflow1.py
# @Software: PyCharm
class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)  ##??? 这种用法第一次见, 作用原理/作用流程是什么?
        # 返回一个父类的实例,然后调用其方法
        # 关键是: super(SubPerson, SubPerson) 如何使用的?

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)
s = SubPerson("laf")