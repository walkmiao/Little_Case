#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 9:27
# @Author  : LCH
# @Site    : 
# @File    : 枚举类.py
# @Software: PyCharm
from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Fri=4
    Sat=5
print(Weekday.Mon,''.center(10,'*'),Weekday.Mon.value)
for k,v in Weekday.__members__.items():
    print('Item:{0}\nValue:{1}'.format(k,v.value))