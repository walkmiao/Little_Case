#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 9:40
# @Author  : LCH
# @Site    : 
# @File    : 多进程.py
# @Software: PyCharm
from multiprocessing import Process,Pool,Queue
import os,time,random
#case -1

# def f(name):
#     print('child process %s(%s)  start!' % (name, os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print('process %s(%s) cost %.2fs'%(name,os.getpid(),end-start))
# if __name__=='__main__':
#     print('Parent process %s...'%os.getpid())
#     p=Pool()
#     for i in range(5):
#         p.apply_async(f,args=(i,))
#     print('waiting for all subprocess done!')
#     p.close()
#     p.join()
#     print('subprocess all done!')

#case -2
def write(q):
    print('Write process %s start..'%os.getpid())
    for i in ['A','B','C']:
        print('put %s to queue..'%i)
        q.put(i)
        time.sleep(random.random())
def read(q):
    print('Read process %s start'%os.getpid())
    while q!=None:
        value=q.get()
        print('from queue get value %s'%value)
if __name__=='__main__':
    print('Parent process start %s'%os.getpid())
    q=Queue()
    w=Process(target=write,args=(q,))
    r=Process(target=read,args=(q,))
    w.start()
    r.start()
    w.join()
    r.join()
    print('wr is end!')
