#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 线程间通信.py
# @Author: lch
# @Date  : 2019/1/31
# @Desc  :
import threading


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        self.cond.acquire()

        self.cond.wait()
        print("{} : 在".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 好啊".format(self.name))
        self.cond.notify()

        self.cond.wait()
        print("{} : 不聊了，再见".format(self.name))
        self.cond.notify()

        self.cond.release()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        self.cond.acquire()

        print("{} : 小爱同学".format(self.name))
        self.cond.notify()
        self.cond.wait()

        print("{} : 我们来对古诗吧".format(self.name))
        self.cond.notify()
        self.cond.wait()

        print("{} : 我住长江头".format(self.name))
        self.cond.notify()
        self.cond.wait()

        self.cond.release()


if __name__ == "__main__":
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    xiaoai.start()
    tianmao.start()

# 执行结果
# 天猫精灵 : 小爱同学