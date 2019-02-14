#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : myRange.py
# @Author: lch
# @Date  : 2018/11/14
# @Desc  :


def my_range(start=None, stop=None, step=1):
    if start != None:
        if stop != None:
            flag = (stop-start)//step if (stop-start) % step == 0 else (stop-start)//step + 1
            my_list = []
            while flag > 0:
                my_list.append(start)
                start = start + step
                flag = flag - 1
            return my_list
        else:
            return my_range(0, start, 1)
    else:
        raise TypeError("expected 1 arguments")


# print(my_range(0,10,2))
print(my_range(10,0,-3))
# print(list(range(0,10,2)))
print(list(range(10,0,-3)))
print(my_range(0,11,5))