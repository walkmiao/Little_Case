#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 普通锁解决不了的问题.py
# @Author: lch
# @Date  : 2019/2/1
# @Desc  :
import threading
import time, random

class XiaoAi(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="小爱")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("{} : 在".format(self.name))
        self.lock.release()
        # time.sleep(0.0001)
        self.lock.acquire()
        print("{} : 好啊".format(self.name))
        self.lock.release()

class TianMao(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="天猫精灵")
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("{} : 小爱同学".format(self.name))
        self.lock.release()
        # time.sleep(0.0001)
        self.lock.acquire()
        print("{} : 我们来对古诗吧".format(self.name))
        self.lock.release()


if __name__ == "__main__":
    lock = threading.Lock()
    xiaoai = XiaoAi(lock)
    tianmao = TianMao(lock)

    tianmao.start()
    xiaoai.start()