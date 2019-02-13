#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 函数和方法的区别.py
# @Author: lch
# @Date  : 2018/11/30
# @Desc  :


class Test:
    def __init__(self, arg1, arg2):
        self.str = arg1 + arg2

    def funcA():
        print('funcA')

    def funcB(self):
        print('funcB:{}'.format(self))

    # 类方法通常会用来作为实例的生产方法
    @classmethod
    def funcC(cls):
        t_ins = cls('i am', ' old!')
        print(t_ins.str)
        return t_ins

    @staticmethod
    def funcD():
        print('i am static method!')


#  Test.funcA 是function  Test().funcA是method但是其无法执行
print(Test.funcA, Test(1, 1).funcA)

#  Test.funcB 是function  Test().funcB
print(Test.funcB, Test(1, 1).funcB)

# Test.funcB需要传入参数来调用， 而Test().fucB则不需要 本质上method会自动传入self 或者cls 作为method的参数 叫做bound method
# function则没有 必须自己手动传入参数
Test.funcB(Test)
Test(1, 1).funcB()

# 类方法 类和实例均可调用
print(Test.funcC, Test(1, 1).funcC)
t_ins = Test.funcC()
print(t_ins.str)

# 静态方法都是function
print(Test.funcD, Test(1, 1).funcD)
