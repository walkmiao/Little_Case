#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 16:08
# @Author  : LCH
# @Site    : 
# @File    : 生成器send方法.py
# @Software: PyCharm
import time
def consumer():
    r=''
    while True:
        n=yield r
        print('[c] Consumer %s..'%n)
        r='200ok'+str(n)

def product(c):
    c.send(None)
    n=0
    while n<5:
        n+=1
        print('[p] Product %s'%n)
        time.sleep(0.5)
        r=c.send(n)
        time.sleep(0.5)
        print('[p] Consumer return:%s'%r)
    c.close()
c=consumer()
product(c)
