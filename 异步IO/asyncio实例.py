#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : asyncioshili.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :
import threading
import asyncio
import time
import functools
now=lambda :time.time()
async def do_some_work(x):
    print('waiting for %d s'%x)
    await asyncio.sleep(x)
    return ('Done after %d s'%x)
def callback(a,future):
    print(a+future.result())

async def main(param):
    coroutine1=do_some_work(1)
    coroutine2=do_some_work(2)
    coroutine3=do_some_work(4)
    task=[asyncio.ensure_future(coroutine1),
          asyncio.ensure_future(coroutine2),
          asyncio.ensure_future(coroutine3)
          ]
    print('main(%s) is running...'%param)
    done,pending=await asyncio.wait(task)
    for task in done:
        print('Task:%s'%task.result())
    return 'task over...'

start=now()
loop=asyncio.get_event_loop()
m1=asyncio.ensure_future(main(1))
m2=asyncio.ensure_future(main(2))
m=[m1,m2]
for i in m:
    i.add_done_callback(functools.partial(callback,'warning!'))
loop.run_until_complete(asyncio.wait(m))
print('cost %s s'%(now()-start))