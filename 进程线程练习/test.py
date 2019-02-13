#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 21:32
# @Author  : LCH
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from multiprocessing import Process, Pool
import os
import time


def consumer():
    r=''
    while True:
        n = yield r
        print('[c]consumer %s'%n)
        r='%s ok'%n
    pass


def produce(c):
    c.send(None)
    for i in range(5):
        print('[p]produce %s'%i)
        n=c.send(i)
        print('[p consumer %s]'%n)
    c.close()
c=consumer()
produce(c)