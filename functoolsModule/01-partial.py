#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 01-partial.py
# @Author: lch
# @Date  : 2019/1/30
# @Desc  :
import random

def partial_use(name, age):
    return "{} is {} old".format(name,age)



def partial_random(num):
    tag_num = random.randint(1,50)
    if num == tag_num:
        return 'bingo'
    return tag_num

class MyPartial:
    def __init__(self, f, *args, **kw):
        self.f = f
        self.args = args
        self.kw = kw

    def __call__(self, *args, **kwargs):
        return self.f(*self.args, *args, **self.kw, **kwargs)


# func = MyPartial(partial_use, 18, 'hh')
# print(func())

func2 = MyPartial(partial_random, 8)

r = iter(func2, 'bingo')

for i in r:
    print(i)
