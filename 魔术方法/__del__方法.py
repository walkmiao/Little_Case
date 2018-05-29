#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 23:50
# @Author  : lch
# @File    : __del__方法.py
'''
__del__当程序结束后，所有的实例将被析构调用del函数
'''
class NewClass(object):
    num_count = 0  # 所有的实例都共享此变量，即不单独为每个实例分配

    def __init__(self, name):
        self.name = name
        NewClass.num_count += 1
        print(name, NewClass.num_count)

    def __del__(self):
        self.__class__.num_count -= 1
        print("Del", self.name, NewClass.num_count)

    @staticmethod
    def test():
        print("aa")


aa = NewClass("Hello")
bb = NewClass("World")
cc = NewClass("aaaa")

print("Over")