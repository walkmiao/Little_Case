#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : my_generator.py
# @Author: lch
# @Date  : 2018/9/27
# @Desc  :
g = (x for x in range(5))
li = [x for x in range(10,15)]
print(g)
for i in g:
    print(i)
for i in g:
    print(i)

for a in li:
    print(a)

for a in li:
    print(a)


def create_generator():
    my_list = [x for x in range(5)]
    for i in my_list:
        yield i*i

my_generator = create_generator()
print(my_generator)

for j in my_generator:
    print(j)