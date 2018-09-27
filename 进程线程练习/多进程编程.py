#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 多进程编程.py
# @Author: lch
# @Date  : 2018/8/22
# @Desc  :
import os
import time
print('before fork process pid=%s, ppid=%s' %(os.getpid(),os.getppid()))
pid = os.fork()
if pid==0:
    print('in child process ,pid=%s, ppid=%s' %(os.getpid(),os.getppid()))
    time.sleep(2)
if pid>0:
    print('in father process ,pid=%s, ppid=%s' %(os.getpid(), os.getppid()))
    time.sleep(2)
print('after fork process , pid=%s, ppid=%s' %(os.getpid(),os.getppid()))

