#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 生产者-消费者模型代码.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :

#协程通过generator实现函数的跳转

def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('[Consumer]Consumer %d'%n)
        r='200 ok'


def produce(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print('[Produce]Producing %d'%n)
        r=c.send(n)
        print('[Produce]Consumer return %s'%r)
    c.close()

c=consumer()
produce(c)
