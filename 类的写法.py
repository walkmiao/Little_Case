#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 18:12
# @Author  : LCH
# @Site    :
# @File    : 类的写法.py
# @Software: PyCharm


class Student(object):
    def __init__(self, age, hight, score=150):
        if age > 10:
            self.__age = age
        if hight > 100:
            self.__hight = hight
        self.__score = score
    # 以装饰器来实现实例的属性访问

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 10:
            self.__age = age
    # 装饰器的另一中写法

    def get_hight(self):
        return self.__hight

    def set_hight(self, hight):
        if hight > 100:
            self.__hight = hight
    hight = property(get_hight, set_hight)
    # 只读属性设置

    @property
    def score(self):
        return self.__score
    # 实例方法

    def get_info(self):
        print('show info'.center(25, '*'))
        print('the age is %s,hight is %s,score is %s' %
              (self.__age, self.__hight, self.score))
    # 类方法

    @classmethod
    def show_classmethod(cls):  # cls代表类本身,self代表实例。当然你可以把self,class_self换成任何名称
        print('this is a Class Method!')

    @staticmethod
    def show_staticmethod():
        print('this a Static Method!')
    # 魔术方法之数学魔术方法

    def __add__(self, other):
        return self.__age + other.__age
    # 魔术方法之打印对象信息

    def __str__(self):
        return 'instance of Student '

    def __repr__(self):  # repr用于交互式编译显示
        return 'instance of Student without print'


s1 = Student(age=12, hight=101)
s1.age = 20
s1.hight = 110
print("Instance Init".center(25, '*'))
print(s1.age, s1.hight, s1.score)
s1.get_info()
print("Class Method Can Call by Class self or Instance".center(70, '*'))
Student.show_classmethod()
s1.show_classmethod()
print("Static Method Can Call by Class self or Instance".center(70, '*'))
Student.show_staticmethod()
s1.show_staticmethod()
print("数学魔术方法之__add__".center(30, '*'))
s2 = Student(15, 102)
print(s1 + s2)
print(s1.__add__(s2))
print(s1)
