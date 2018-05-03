#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 16:20
# @Author  : LCH
# @Site    : 
# @File    : 编码解码.py
# @Software: PyCharm

u='风朝'
#encode 进行编码
s1=u.encode('gbk')
s2=u.encode('gb2312')
s3=u.encode('utf-8')
#编码后的bytes类型对象
print(u)
print(s1)
print(s2)
print(s3)
#再以相应编码来进行解码 不能弄错
print(s1.decode('gbk'))
print(s3.decode('utf-8'))