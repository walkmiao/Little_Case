#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 缓存区刷新.py
# @Author: lch
# @Date  : 2018/8/20
# @Desc  :
import time
import sys
def if_flush():
    for i in range(1,6):
        print(i)
        time.sleep(0.5)

if_flush()