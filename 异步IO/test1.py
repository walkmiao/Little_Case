#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 10:39
# @Author  : LCH
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
import asyncio
import time
now = lambda:time.time()
async def do_some(x):
    print('waiting for %s s to start..'%x)
    await asyncio.sleep(x) # 模拟异步阻塞
    print("do some over")

coro = do_some(2)
# coro2 = do_some(5)
# coro3 = do_some(3)
# task = asyncio.

loop = asyncio.get_event_loop()
task = loop.create_task(coro)
print(task)
start = now()
loop.run_until_complete(task)
print(now()-start)
print(task._state)