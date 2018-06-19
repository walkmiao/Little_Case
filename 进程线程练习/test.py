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


def run_proc(name):
    # print('run child process %s,pid is %s' % (name, os.getpid()))
    # time.sleep(5)
    return ('ceshi'+name)

if __name__ == '__main__':
    pool = Pool()
    print('Parent process %s start'%os.getpid())
    temp=[]
    for i in range(1,10):
        i=str(i)
        temp.append(pool.apply_async(run_proc, args=(i,)))
    print('waiting for all task done...')
    pool.close()
    pool.join()
    print('all task done')
    print(temp)
    for i in temp:
        print(i.get())