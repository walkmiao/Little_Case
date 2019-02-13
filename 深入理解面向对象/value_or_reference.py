#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : value_or_reference.py
# @Author: lch
# @Date  : 2018/9/27
# @Desc  :
class PassByReference:
    def __init__(self):
        self.value = 'Original'
        self.reference = []
        self.change(self.value, self.reference)
        print(self.value,self.reference)

    def change(self, var, refer):
        var = 'Changed'
        refer.append(1)


p = PassByReference()
