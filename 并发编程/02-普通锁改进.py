#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 02-普通锁改进.py
# @Author: lch
# @Date  : 2019/2/1
# @Desc  :
import threading

class XiaoAi(threading.Thread):
    def __init__(self, lock, active_user):
        super().__init__(name="小爱")
        self.lock = lock
        self.active_user = active_user

    def wait(self):
        while(1):
            self.lock.acquire()
            user = self.active_user[0]
            self.lock.release()
            if user == 1:
                break

    def notify(self):
        self.lock.acquire()
        self.active_user[0] = 0
        self.lock.release()

    def run(self):
        self.wait()
        print("{} : 在".format(self.name))
        self.notify()

        self.wait()
        print("{} : 好啊".format(self.name))
        self.notify()

class TianMao(threading.Thread):
    def __init__(self, lock, active_user):
        super().__init__(name="天猫精灵")
        self.lock = lock
        self.active_user = active_user

    def wait(self):
        while(1):
            self.lock.acquire()
            user = self.active_user[0]
            self.lock.release()
            if user == 0:
                break

    def notify(self):
        self.lock.acquire()
        self.active_user[0] = 1
        self.lock.release()

    def run(self):
        self.wait()
        print("{} : 小爱同学".format(self.name))
        self.notify()

        self.wait()
        print("{} : 我们来对古诗吧".format(self.name))
        self.notify()


if __name__ == "__main__":
    # 0表示天猫执行， 1表示小爱
    # 为了保证两个线程修改active_user之后,互相是可见的，所以传了一个List,而不是整数
    active_user = [0]
    lock = threading.Lock()
    xiaoai = XiaoAi(lock, active_user)
    tianmao = TianMao(lock, active_user)

    tianmao.start()
    xiaoai.start()