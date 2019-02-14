#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串IO操作.py
# @Author: lch
# @Date  : 2019/1/31
# @Desc  :
import io

s = io.StringIO("hello\n")
print(s.read(2))
print(s.read())