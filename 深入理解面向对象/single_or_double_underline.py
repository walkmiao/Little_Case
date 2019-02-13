#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : single_or_double_underline.py
# @Author: lch
# @Date  : 2018/9/27
# @Desc  :
class UnderLine:
    def __init__(self):
     self.__double = 'double underline '
     self._single =  'single underline '
    def test(self):
        pass

c = UnderLine()
print(c.__dict__)
print(dir(c))
print(c._UnderLine__double)
print(c._single)
