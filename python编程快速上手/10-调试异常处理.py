#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 8:58
# @Author  : LCH
# @Site    : 
# @File    : 10-调试异常处理.py
# @Software: PyCharm
import traceback
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s -%(message)s')
#通常是调用该函数的代码知道如何处理异常，而不是该函数本身

# def div(a,b):
#     if b==0:
#         raise Exception('this value can\'t be zero')
# try:
#     div(10,0)
# except Exception as err:
#     print(err)

#反向跟踪字符串
"""" 
def a():
     b()
def b():
     raise Exception('test error!')
 
a()"""

#使用traceback.format_exc()

# try:
#     raise Exception('this is an error message!')
# except:
#     errorfile=open('err.txt','w')
#     errorfile.write(traceback.format_exc())
#     errorfile.close()
#     print('end')
#

#assert 断言
# a='new'
# assert a=='ew','a is not new!'

#日志模块
#计算阶乘
def f(a):
    if a==1:
        return 1
    return a*f(a-1)
print(f(5))
