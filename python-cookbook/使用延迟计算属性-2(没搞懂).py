#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 使用延迟计算属性-2.py
# @Author: lch
# @Date  : 2019/2/19
# @Desc  :
import math


def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
    return lazy


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(2)
print(c.radius)
print(c.area)
print(c.area)
c.area=12
