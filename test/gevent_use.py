#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : gevent_use.py
# @Author: lch
# @Date  : 2018/8/20
# @Desc  :
import gevent

def foo():
    print('excute foo...')
    gevent.sleep(1)
    print('switch to foo again!')

def bar():
    print('switch to bar, excute bar...')
    gevent.sleep(1)
    print('switch to bar again!')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),]
)