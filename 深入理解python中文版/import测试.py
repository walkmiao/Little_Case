#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : import测试.py
# @Author: lch
# @Date  : 2018/8/16
# @Desc  :
import sys
import os
c_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(c_path)
import database_param
print(dir(database_param.build_connect_string))
print(database_param.build_connect_string.__dict__)
print(getattr(database_param.build_connect_string, '__dict__'))
print(dir({}))