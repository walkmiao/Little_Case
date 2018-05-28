#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 进程池和线程池.py
# @Author: lch
# @Date  : 2018/5/23
# @Desc  :
# from multiprocessing import Pool
# import time,random,os
# def func(n):
#     print('task[%s] running(%s)..'%(n,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     print('task[%s] cost %s'%(n,time.time()-start))
# if __name__=='__main__':
#     pool=Pool(4)
#     results=[]
#     for i in range(10):
#         result=pool.apply_async(func,args=(i,))
#         results.append(result)
#     pool.close()
#     pool.join()
#     print('all task in done..')

import multiprocessing
import time


def func(msg):
    print('msg: ', msg)
    time.sleep(1)
    print('********')
    return 'func_return: %s' % msg

if __name__ == '__main__':
    # apply_async--异步非阻塞
    print('\n--------apply_async------------')
    pool = multiprocessing.Pool(processes=4)
    results = []
    for i in range(10):
        msg = 'hello world %d' % i
        result = pool.apply_async(func, (msg, ))
        results.append(result)
    print('apply_async: 不堵塞')

    for i in results:
        i.wait()
    for i in results:
        if i.ready():
            if i.successful():
                print(i.get())

    # for i in results:
    #     i.wait()  # 等待进程函数执完毕
    #
    # for i in results:
    #     if i.ready():  # 进程函数是否已经启动了
    #         if i.successful():  # 进程函数是否执行成功
    #             print(i.get())  # 进程函数返回值

    # apply--阻塞式 先运行主进程，至子进程时 子进程按顺序一个接一个运行，运行完毕后再切到主进程
    print('\n--------apply------------')
    pool = multiprocessing.Pool(processes=4)
    results = []
    for i in range(10):
        msg = 'hello world %d' % i
        result = pool.apply(func, (msg,))
        results.append(result)
    print('apply: 堵塞')  # 执行完func才执行该句
    pool.close()
    pool.join()  # join语句要放在close之后
    print(results)

    # map
    print('\n--------map------------')
    args = [1, 2, 4, 5, 7, 8]
    pool = multiprocessing.Pool(processes=5)
    return_data = pool.map(func, args)
    print('堵塞')  # 执行完func才执行该句
    pool.close()
    pool.join()  # join语句要放在close之后
    print(return_data)

    # map_async
    print('\n--------map_async------------')
    pool = multiprocessing.Pool(processes=5)
    result = pool.map_async(func, args)
    print('ready: ', result.ready())
    print('不堵塞')
    result.wait()  # 等待所有进程函数执行完毕

    if result.ready():  # 进程函数是否已经启动了
        if result.successful():  # 进程函数是否执行成功
            print(result.get())  # 进程函数返回值