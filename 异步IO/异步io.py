#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 16:44
# @Author  : LCH
# @Site    : 
# @File    : asyncio.py
# @Software: PyCharm
import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
