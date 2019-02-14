#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 02-reduce.py
# @Author: lch
# @Date  : 2019/1/31
# @Desc  :
from functools import reduce, partial
from collections import Iterable
import time

exam = range(1, 10000000)


class CalTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        t1 = time.time()
        r = self.func(*args, **kwargs)
        result = r if not callable(r) else r()
        t2 = time.time()
        print("cost time {} s".format(t2-t1))
        return result


@CalTime
def call_reduce():
    r = reduce(lambda x, y: x+y, exam)
    return r


@CalTime
class MyReduce:
    def __init__(self, f, can_iter):
        if not isinstance(can_iter, Iterable):
            raise Exception("{} is not iterable...".format(can_iter))
        self.f = f
        self.i = can_iter

    def get_para(self):
        for p in self.i:
            yield p

    def get_result(self):
        cache = list()
        for i in self.get_para():
            cache.append(i)
            if len(cache) == 2:
                temp = self.f(cache[0], cache[1])
                cache.clear()
                cache.append(temp)
        return cache[0]

    def __call__(self, *args, **kwargs):
        return self.get_result()


c1 = call_reduce()
c2 = MyReduce(lambda x, y: x+y, exam)
print(c1, c2)



