#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 设计指定长度随机密码.py
# @Author: lch
# @Date  : 2018/10/10
# @Desc  :
"""

题目2: 设计一个函数，生成指定长度的验证码（由数字和大小写英文字母构成的随机字符串）

"""
import random

def generate_code(length=6):
    caplize = [ chr(i) for i in range(ord('a'), ord('z')+1)]
    low = [ chr(i) for i in range(ord('A'), ord('Z')+1)]
    num_list = [i for i in range(10)]
    len_cap = random.randint(1, length-2)
    len_low = random.randint(1, length-len_cap-1)
    len_num = length - len_cap - len_low
    return random.sample(caplize, len_cap) + random.sample(low, len_low) + random.sample(num_list, len_num)

print(generate_code())



