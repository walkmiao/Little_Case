#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 16:16
# @Author  : LCH
# @Site    : 
# @File    : 7.18.1-7.18.2.py
# @Software: PyCharm

#7.18.1 暂未实现
import re
def pwTest(password):
    pass

#7.18.2,用正则实现strip()函数功能，并能通过第二个参数 删除指定字符后返回
def stripNew(charater,para=None):
    regex = re.compile(r'\s*(\b.*\b)\s*')
    match = regex.match(charater)
    if match:
        match = match.group(1)
        if para==None:
            return match
        else:
            r=re.compile(para)
            match=r.sub('',match)
            return match



s1='  i am a python learner!'
s2='how are you!     '
s3='  do what you want to do   '
print('只有一个参数'.center(20,'#'))
print(stripNew(s1))
print(stripNew(s2))
print(stripNew(s3))
print('两个参数'.center(20,'#'))
print(stripNew(s1,'a'))
print(stripNew(s2,'o'))
print(stripNew(s3,'t'))



