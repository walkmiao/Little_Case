#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 对类中方法的装饰.py
# @Author: lch
# @Date  : 2018/11/28
# @Desc  :


def test_decorator(func):
    def wrap(self):
        print('method {} is decorated'.format(func.__name__))
        print(self)
        return func(self)
    return wrap


def method_to_function(decorator_func):
    pass


class Info:
    def __init__(self):
        self.info = 'new info'

    @test_decorator
    def show_info(self):
        print(self.info)


info = Info()
print('info->{}'.format(info))
info.show_info()



