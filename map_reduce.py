#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 11:05
# @Author  : LCH
# @Site    : 
# @File    : map_reduce.py
# @Software: PyCharm
from functools import reduce
print('map函数打印'.center(20,'*'))
L1=map(lambda x:('整数'+str(x)),[x for x in range(1,10) if (x%2==0)])
for i in L1:
    print(i)
print('reduce 函数打印'.center(20,'*'))
L2=reduce(lambda x,y:x*y,[x for x in range (1,10) if (x%2==0)])
print(L2)
print('分割线'.center(20,'-'))
print('fileter 函数打印'.center(20,'*'))
def f(x):
    if x%2==0:
        return x
L3=filter(lambda x:f(x),[x for x in range(1,10)])
for i in L3:
    print(i)
print('sorted函数打印'.center(20,'*'))
L4=sorted([x for x in range(1,10)],key=abs)
for i in L4:
    print(i)

