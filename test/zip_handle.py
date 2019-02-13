#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : zip_handle.py
# @Author: lch
# @Date  : 2018/9/18
# @Desc  :

nums = ['flower']
s = zip(*nums)
print(s)
for i in zip(*nums):
    print(i)
