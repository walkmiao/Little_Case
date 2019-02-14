#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 深浅赋值.py
# @Author: lch
# @Date  : 2018/10/12
# @Desc  :
import weakref
import array

class Vector2d():
    type_code = 'd'
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __add__(self, other):
        print(self, other)
        return Vector2d(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        return "{cls}({!r},{!r})".format(cls=self.__class__.__name__, *self)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __bytes__(self):
        return (bytes([100]) +
                bytes(array.array(self.type_code, self)))





a = Vector2d(3,4)
b = Vector2d(1,2)
print(a)
print(b)
print(a+b)
a_clone = eval(repr(a))
print(a_clone == a)
x,y = a
print(x,y)
print(iter(a))
print(a==b)
print(bytes(a))
print(bytes(100))
print(bytes([100]))
