#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 16:16
# @Author  : LCH
# @Site    : 
# @File    : 7.18.1-7.18.2.py
# @Software: PyCharm

#7.18.1 实现对口令的强度检测，直到口令强度达到后停止程序
import re
def pwTest():
    password=input('input your passwd:\n')
    regex1=re.compile(r'[a-z]+')
    regex2=re.compile(r'[A-Z]+')
    regex3=re.compile(r'\d+')
    if len(password)>8 and regex1.search(password) and regex2.search(password) and regex3.search(password):
        print('password is strong!')
    else:
        print('check password!')
        pwTest()



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


