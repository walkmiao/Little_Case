#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 1.py
# @Author: lch
# @Date  : 2018/8/20
# @Desc  :
'''
打印斐波那契数列 112358
'''
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    num = int(input('请输入所需打印项数:'))
    if num<0:
        print('必须输入大于0的整数')
    for i in range(1,num+1):
        print(fib(i))



