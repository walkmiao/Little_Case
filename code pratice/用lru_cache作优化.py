#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 用lru_cache作优化.py
# @Author: lch
# @Date  : 2018/10/10
# @Desc  :
'''
计算第n个斐波拉契数值
'''
import time
import functools
num = 0
def list_call_num(func):
    def wrapper(*args):
        result = func(*args)
        print('%s(%s)->%s' %(func.__name__, args,result))
        return result
    return wrapper
@functools.lru_cache()
@list_call_num
def fib(n):
    global num
    num = num + 1
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    t1 = time.time()
    fib(30)
    print('耗时%s'%(time.time()-t1))
    print('call times %s' % num)