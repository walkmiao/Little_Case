#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 16:08
# @Author  : lch
# @File    : 杨辉三角打印.py
#获取杨辉三角函数
def get_angela(n):
    L = [1]
    while n>1:
        yield L
        L = [x + y for x, y in zip([0] + L, L + [0])]
        n=n-1

for i in get_angela(10):
    print(i)