#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 当继承了dict.py
# @Author: lch
# @Date  : 2018/10/11
# @Desc  :

class User(dict):
    pass

d = User(name='lch', age=10)
print(d)