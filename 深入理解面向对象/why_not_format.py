#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : why_not_format.py
# @Author: lch
# @Date  : 2018/9/27
# @Desc  :
import random
s1 = ' ugly'
s2= 'betiful'
print('this is %s' % s1)
print('this is %(arg)s' %{'arg':s1})
print('this is {}'.format(s2))
print('this is {arg2}'.format(**{'arg2': s2}))

'''
map is so useful！ just like below
'''
li = [i for i in range(11)]
for i in map('the num is {}'.format,  li):
    print(i)
