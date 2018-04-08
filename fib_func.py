#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 13:50
# @Author  : lch
# @File    : fib_func.py

# 斐波拉契数列获取


def fib_func(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'Down!'


g = fib_func(6)
while True:
    try:
        print(g.__next__())
    except StopIteration as e:
        print(e.value)
        break
