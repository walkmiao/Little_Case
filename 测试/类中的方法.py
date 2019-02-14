#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 类中的方法.py
# @Author: lch
# @Date  : 2019/1/31
# @Desc  :


class Demo:
    def generic_method(self):
        return 'call generic_method, para is %s' % self

    @classmethod
    def class_method(cls):
        return 'call class_method, para is %s' % cls

    @staticmethod
    def static_method():
        return 'i am just a static method, in react i am a function'


demo = Demo()
print(demo.generic_method, demo.generic_method(), sep=' 结果为: ', end='\n')
print(Demo.generic_method, Demo.generic_method(demo), sep=' 结果为: ', end='\n')
print('*'*50)
print(Demo.class_method, Demo.class_method(),  sep=' 结果为: ', end='\n')
print(demo.class_method, demo.class_method(), sep=' 结果为: ', end='\n')
print('*'*50)
print(Demo.static_method, Demo.static_method(), sep=' 结果为: ', end='\n')
print(demo.static_method, demo.static_method(), sep=' 结果为: ', end='\n')
