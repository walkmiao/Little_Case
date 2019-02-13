#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 异常处理.py
# @Author: lch
# @Date  : 2018/8/20
# @Desc  :
import logging
try:
    fs = open('/fs')
except IOError:
    logging.warn('dont exist this file')
print('this line will always print')