#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 字符串中出现个数.py
# @Author: lch
# @Date  : 2018/10/10
# @Desc  :
"""

题目3: 设计一个函数，统计字符串中英文字母和数字各自出现的次数

"""
import re
import logging
logging.basicConfig(level=logging.INFO)
def cal_str(s):
    r = re.compile(r'\d|\w')
    d = {}
    for i in s:
        if r.match(i):
            d[i] = d.setdefault(i, 0) + 1

    for i, j in d.items():
        print("[{}]:{}" .format(i , j))


if __name__ == '__main__':
    s = input("输入你的字符串：")
    logging.info('----统计结果-----')
    cal_str(s)
