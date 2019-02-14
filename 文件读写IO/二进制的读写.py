#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 二进制的读写.py
# @Author: lch
# @Date  : 2019/1/31
# @Desc  :
import array

with open('demo1.txt', 'wb') as f:
    arr = array.array('i', [1, 2, 3])
    f.write(arr)

with open('demo1.txt', 'rb') as f2:
    s = f2.read()
    print(s.decode())
