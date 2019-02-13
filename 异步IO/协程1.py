#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 协程1.py
# @Author: lch
# @Date  : 2018/8/17
# @Desc  :
import asyncio
import time


async def do_work(x):
    print('wait:%s' % x)
    await asyncio.sleep(x)
    return 'Done after {} s'.format(x)


def call_back(future):
    print('%s callback:%s' % (future, future.result()))


now = lambda: time.time()
start = now()
corotine1 = do_work(1)
corotine2 = do_work(2)
corotine3 = do_work(4)
loop = asyncio.get_event_loop()
tasks = [loop.create_task(corotine1),
         loop.create_task(corotine2),
         loop.create_task(corotine3)]
for task in tasks:
    task.add_done_callback(call_back)
# loop.run_until_complete(asyncio.gather(*tasks))
loop.run_until_complete(asyncio.wait(tasks))

print('cost %f s' % (time.time()-start))
