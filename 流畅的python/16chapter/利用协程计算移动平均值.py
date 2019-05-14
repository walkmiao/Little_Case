#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 利用协程计算移动平均值.py
# @Author: lch
# @Date  : 2019/2/27
# @Desc  :
import inspect


def active_gen(func):
    def wrap(*args, **kw):
        gen = func(*args, **kw)
        gen.send(None)
        return gen
    return wrap

@active_gen
def cal_avg():
    total = 0
    count = 0
    avg = None
    while True:
        s_val = yield avg
        count += 1
        total = total + s_val
        avg = total/count



gen = cal_avg()

# gen.send(None) #必须首先激活生成器，如果害怕忘记可以使用装饰器来保证预激生成器
print(gen.send(12))