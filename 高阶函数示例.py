#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 10:39
# @Author  : LCH
# @Site    : 
# @File    : 高阶函数示例.py
# @Software: PyCharm
from functools import reduce
'''这是我写的一种方法，把字符串转换为浮点数
'''
# def str2float(s):
#     if '.' in s:
#         index=s.index('.')
#         print(index)
#         print(s[:index],s[index+1:])
#         i=reduce(lambda x,y:x*10+y,map(int,s[:index]))
#         j=reduce(lambda x,y:x*10+y,map(int,s[index+1:]))
#         print(i,j)
#         return i+(j/(10**(len(s)-1-index)))

#这是另外一种方法，两种方法均可以实现
def str2float(s):
    return reduce(lambda x, y: x + y / (10 ** (len(str(y)))), map(int, s.split('.')))
print(str2float('125.3467'))
print(list(map(int,'123.456'.split('.'))))

'''下面是filter函数，filter参数也是一个函数和一个序列，并把序列中的每个元素作用在函数上。不同的是它是跟据
    返回值来判断元素是否保留，从而返回一个新的序列
'''
l=range(1,20)
print(list(filter(lambda x:x%2==0,l)))
s=['a',' ','s',None,'gru']
print(list(filter(lambda x:x and x.strip(),s)))
print(str(123))
print(str(123)[-1::-1])

