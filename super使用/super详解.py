#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 11:08
# @Author  : LCH
# @Site    : 
# @File    : super详解.py
# @Software: PyCharm

import logging
logging.basicConfig(level=logging.INFO)
from functools import partial

class A:
    def show(self):
        print('i am A')


class B:
    def show(self):
        print('i am B')

    @classmethod
    def cls_meth(cls):
        print(' i am B classmethod')
        print('cls is {}'.format(cls))


class C(B):
    def __init__(self):
        s = super(C)
        print(s)
    def __str__(self):
        print(dir(C))
        return 'i am C ...'
    __repr__ = __str__
    pass


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('set item key={}, value={}'.format(key, value))
        super(LoggingDict, self).__setitem__(key, value)

    def __getitem__(self, item):
        return super(LoggingDict, self).__getitem__(item)


log = LoggingDict()
log[1] = 'angela'
print(log[1])
c = C()
