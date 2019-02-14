#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : demo2.py
# @Author: lch
# @Date  : 2018/11/28
# @Desc  :
try:
    from demo import DemoClass
    d = DemoClass()
    d.public_method()
    d._light_private_method()
except Exception as e:
    print(e)