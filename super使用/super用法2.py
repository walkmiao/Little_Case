#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 13:46
# @Author  : LCH
# @Site    : 
# @File    : super用法2.py
# @Software: PyCharm


class Root:
    def show(self):
        s = super()
        print(s)
        assert not hasattr(super(), 'show')


class Shape(Root):
    def __init__(self, name, **kw):
        self.name = name
        super().__init__(**kw)

    def show(self):
        super().show()


class ColorShape(Shape):
    def __init__(self, color, **kw):
        self.color = color
        super().__init__(**kw)

    def show(self):
        print('color is {}'.format(self.color))
        super().show()


c = ColorShape(color='blue', name='new_shape')
c.show()