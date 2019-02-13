#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 单例模式.py
# @Author: lch
# @Date  : 2018/7/2
# @Desc  :


class Sington():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'): # 当然这里instance你可以换成其他的变量，只要cls中没有这个属性即可
            cls.instance = super(Sington, cls).__new__(cls, *args, **kwargs)
        return cls.instance


a = Sington()
a.title = 'a title'
b = Sington()
print(a is b, b.title)
