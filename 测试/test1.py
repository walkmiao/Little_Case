#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test1.py
# @Author: lch
# @Date  : 2018/6/19
# @Desc  :
from django.db import models
# 简单的dict
d={1:['a','b','c'],2:['e','f','g']}
d=dict(d)
l=[(k,v) for k,v in d.items()]
print(l)
lst = [('d', 2), ('a', 4), ('b', 3), ('c', 2)]

# 按照value排序
lst.sort(key=lambda k: k[1])
print(lst)
