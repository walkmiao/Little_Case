#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :
# -*-coding:utf-8-*-
import threading

mutex_lock = threading.RLock()  # 互斥锁的声明
ticket = 100000  # 总票数
# 用于统计各个线程的得票数
ticket_for_thread1 = 0
ticket_for_thread2 = 0
ticket_for_thread3 = 0
ticket_for_thread4 = 0


class MyThread(threading.Thread):  # 线程处理函数
    def __init__(self, name):
        threading.Thread.__init__(self)  # 线程类必须的初始化
        self.thread_name = name  # 将传递过来的name构造到类中的name

    def run(self):
        # 声明在类中使用全局变量
        global mutex_lock
        global ticket
        global ticket_for_thread1
        global ticket_for_thread2
        global ticket_for_thread3
        global ticket_for_thread4
        while True:
            mutex_lock.acquire()  # 临界区开始，互斥的开始
            # 仅能有一个线程↓↓↓↓↓↓↓↓↓↓↓↓
            if ticket > 0:
                ticket -= 1
                # 统计哪到线程拿到票
                print("%s抢到了票！票还剩余：%d。" % (self.thread_name, ticket))
                if self.thread_name == "线程1":
                    ticket_for_thread1 += 1
                elif self.thread_name == "线程2":
                    ticket_for_thread2 += 1
                elif self.thread_name == "线程3":
                    ticket_for_thread3 += 1
                elif self.thread_name == "线程4":
                    ticket_for_thread4 += 1
            else:
                break
                # 仅能有一个线程↑↑↑↑↑↑↑↑↑↑↑↑
            mutex_lock.release()  # 临界区结束，互斥的结束
        mutex_lock.release()  # python在线程死亡的时候，不会清理已存在在线程函数的互斥锁，必须程序猿自己主动清理
        print("%s被销毁了！" % (self.thread_name))

    # 初始化线程


thread1 = MyThread("线程1")
thread2 = MyThread("线程2")
thread3 = MyThread("线程3")
thread4 = MyThread("线程4")
# 开启线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
# 等到线程1、2、3、4结束才进行以下的代码（同步）
thread1.join()
thread2.join()
thread3.join()
thread4.join()
print("票都抢光了，大家都散了吧！")
print("=========得票统计=========")
print("线程1：%d张" % (ticket_for_thread1))
print("线程2：%d张" % (ticket_for_thread2))
print("线程3：%d张" % (ticket_for_thread3))
print("线程4：%d张" % (ticket_for_thread4))
print(
    "总票数共：%s" %
    (ticket_for_thread1 +
     ticket_for_thread2 +
     ticket_for_thread3 +
     ticket_for_thread4))
