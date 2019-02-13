#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 类说明.py
# @Author: lch
# @Date  : 2018/10/11
# @Desc  :
class Test:
    def __init__(self,length):
        self.length = length

    def something(self):
        if self.length>10:
            wtf='a'
        else:
            pass
        return wtf

t = Test(10)
print(t.something())

