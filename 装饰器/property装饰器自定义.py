#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 17:32
# @Author  : LCH
# @Site    : 
# @File    : property装饰器自定义.py
# @Software: PyCharm
# 装饰类
class MyProperty(object):
    def __init__(self, get, set=None):
        self.__get = get
        self.__set = set

    def __get__(self, inst, type=None):
        return self.__get(inst)

    def __set__(self, inst, value):
        if self.__set is None:
            raise AttributeError("this attribute is read-only")
        return self.__set(inst, value)

    # 对象.setter的装饰函数
    def setter(self, set):
        self.__set = set
        return self


# -------------------------------------------------------------
# 装饰函数，在两个类的外面
def property(func):
    # 用和func相同的名称创建一个MyProperty类的实例并返回
    exec(func.__name__ + '=MyProperty(func)')
    return eval(func.__name__)


# ------------------------------------------------------------

# 实现类举例，和内置@property一致语法
class Student(object):
    def __init__(self):
        self._score = 8

    # 读取方法装饰
    @property
    def score(self):
        return self._score

    # 写入方法装饰
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整数才行呐')
        if value < 0 or value > 100:
            raise ValueError('分数必须0-100之间')
        self._score = value


s= Student()
print(s.score)
s.score = 101