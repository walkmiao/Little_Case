#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 10:54
# @Author  : LCH
# @Site    : 
# @File    : 多线程.py
# @Software: PyCharm

#threading 封装了_thread,使用时一般用threading就可达到多线程的目的
# import threading
# b=0
# def test(n):
#     global b
#     b=b+n
#     b=b-n
# def loop(n):
#     for i in range(100):
#         test(n)
# if __name__=='__main__':
#     t1=threading.Thread(target=loop,args=(5,))
#     t2=threading.Thread(target=loop,args=(8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print('end and b=%d'%b)
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



