#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 能否构成等差数列.py
# @Author: lch
# @Date  : 2018/10/10
# @Desc  :
"""

题目4: 设计一个函数，判断传入的整数列表（要求元素个数大于2个）中的元素能否构成等差数列

"""
def f(li, m=0, n=-1):
    length = int(len(li)/2)-1
    print(length)
    while length>0:
        if li[m] + li[n] ==li[m+1] + li[n-1]:
            length -=1
            m = m+1
            n = n-1
        else:
            return False
    return True

def is_dengcha(p_list):
    add = p_list[0] + p_list[-1]
    if len(p_list) % 2==0:
        return f(p_list)
    else:
        mid = p_list[int(len(p_list)/2)]
        if mid*2 == add:
            p_list.remove(mid)
            return True if f(p_list) else False




p_list=[ i for i in range(4) if i%2==0]
print(p_list)
print(is_dengcha(p_list))


