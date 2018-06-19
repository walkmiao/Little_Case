#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 多线程之setdaemon.py
# @Author: lch
# @Date  : 2018/5/22
# @Desc  :
import threading,time

class Mythread(threading.Thread):
    def __init__(self,id):
        super(Mythread, self).__init__()
        self.id=id
    def run(self):
        time.sleep(3)
        print(self.id)

if __name__=='__main__':
    s=Mythread(999)
    s.setDaemon(True)#setdaemon和join作用相反,当子线程设置setdaemon 相当于主线程是守护线程。当主线程结束时不会再等待子线程完成。而是直接结束
    s.start()
    # s.join() #在主线程中，子线程join会让主线程一直等待子线程工作完成，才继续主线程的工作
    for i in range(5):
        print(i)