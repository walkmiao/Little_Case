#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 生产者消费者.py
# @Author: lch
# @Date  : 2018/5/27
# @Desc  :
'''
协程是依靠生成器来实现的，生产者消费者正是一个典型的例子
'''

def consumer():
    r=''
    while True:
        n=yield r
        print('[C]consumer %s'%n)
        r='%s ok'%n



def product(c):
    c.send(None)#启动生成器,第一次启动生成器参数必须为None，因为没有yield表达式来接收这个参数值
    n=0
    while n<=5:
        print('[P]produce %s'%n)
        r=c.send(n) #send方法把值传给yield表达式，send方法还会返回下一个yield的值。
        print('[P]return %s'%r)
        n+=1
    c.close()

c=consumer()
product(c)