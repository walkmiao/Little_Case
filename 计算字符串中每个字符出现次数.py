#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 13:17
# @Author  : LCH
# @Site    : 
# @File    : 计算字符串中每个字符出现次数.py
# @Software: PyCharm

#通过使用dict的setdefault方法巧妙计算 字符串中每个字符出现的次数 进而打印出次数最多的字符
s='i am A pure man,i love study,swimming and basketball!'
d={}
for i in s:
    d.setdefault(i,0)
    d[i]=d[i]+1
print('获取到的初始字典'.center(30,'#'))
print(d)
#key value的反转,这里又使用了setdefault，如果d2没有key的话 设置默认值为[] 这样就有了append方法 精彩！
d2={}
for k,v in d.items():
    d2.setdefault(v,[]).append(k)
print('key,value互换后的字典'.center(30,'#'))
print(d2)
print('获取出现次数最多的那个字符')
print(d2[max(d2.keys())])
