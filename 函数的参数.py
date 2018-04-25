#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 16:24
# @Author  : LCH
# @Site    : 
# @File    : 函数的参数.py
# @Software: PyCharm

# NO.1可变参数
def get_result(*pr):
    sum=0
    for i in pr:
        sum=sum+i**2
    return sum
result=get_result(3,5,7,8)
print(result)
list=[3,5,7,8]
print(get_result(*list))

# NO.2 关键字参数
def get_str(name,age,**kw):
    if 'cc' in kw:
        print('city is in this dict!')
    print(name,'/',age,'/',kw)
kw={'city':'beijing','job':'sale'}
get_str('lch',18,city=kw['city'],jobb=kw['job'],cc=kw['city'],bb='nobb')
get_str('lch',20,**kw)