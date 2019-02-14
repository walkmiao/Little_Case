#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : demo.py
# @Author: lch
# @Date  : 2018/11/28
# @Desc  :
from pprint import pprint

class Person(object):
    def __init__(self, name, age, speak):
        self.name = name
        self._age = age  # 使用一个下划线来私有属性'_'
        self.__speak = speak  # 使用两个下划线来私有属性‘_’

    def showperson(self):
        print(self.name, self._age, self.__speak)

    def dowork(self):
        self._work()
        self.__away()

    def _work(self):  # 注意，这是一个下划线修饰的私有方法
        print('my _work')

    def __away(self):  # 注意，这是两个下划线私有的属性
        print('my __away')


class Student(Person):  # Student继承父类Person
    def construction(self, name, age, speak):  # 该防范功能是给属性重新赋值。
        self.name = name
        self._age = age
        self.__speak = speak

    def showstudent(self):
        print(self.name, self._age, self.__speak)

    @staticmethod  # 静态方法，不需要定义参数
    def testbug():
        _Bug.showbug()  # 可以调用了外部的单下划线修饰的模块的方法。


# 单个下划线修饰的“_”的变量、函数、类在使用from xxx import *时都不会被导入
class _Bug(object):  # 单个下划线修饰的私有类。
    @staticmethod
    def showbug():
        print("showbug")


# ------------------------------------------数据测试--------------------------------------

# 1.子类可以调用父类中的公有方法，属性，包括父类的中用单个下划线_修饰的私有属性和方法
s1 = Student('jack', 25, 'Chinese')  # 创建Student的实例s1,因为s1没有__init__方法，调用父类的方法
pprint(dir(s1))
s1.showperson()  # 调用继承父类的showperson()方法
print(s1.name, s1._age)
s1.dowork()
s1._work()
# s1.__away  子类无法访问父类中用两个下划线修饰的私有方法。
# print(s1.__speak) 报错，两个__下划线修饰的属性方法子类无法直接访问。
'''
jack 25 Chinese
jack 25
my _work
my __away
my _work
'''

# 2.子类不能访问父类中两个下划线__修饰的方法和属性，也不能修改父类中双下划线的属性。但是单下划线属性可以修改
# s1.showstudent() 报错，因为子类Student没有定义自己的属性，name,age,speak，都是继承父类的，方法中调用的私有属性不能访问
s1.construction('rose', 30, 'English')  # 子类对继承的属性重新赋值
pprint(dir(s1))

s1.showperson()  # rose 30 Chinese  注意，调用父类的方法，__speak双下划线的属性没有被修改。
# 如果在子类中向__名字赋值，那么会在子类中定义的一个与父类相同名字的属性

s1.showstudent()  # rose 30 English 这里调用子类的自己的方法，__speak被修改了。

Student.testbug()  # showbug


