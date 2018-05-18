#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 回文数.py
# @Author: lch
# @Date  : 2018/5/17
# @Desc  :

def check(num):
    '''
    判断一个数是否为回文数。
    回文数例如11，22，121
    :param num: 检测是否为回文数
    :return: 布尔值
    '''
    num=str(num)
    if num[:]==num[-1::-1]:
        return True
    return False
#回文数颠倒求和
def num_reverse(num):
    num=str(num)
    return int(num[-1::-1])

def get_steps(check):
    step=1
    num=int(input('input your number:'))
    if 12<=num and num<=100 and check(num)==False:
        add_num=num_reverse(num)+num
        is_get = check(add_num)
        while not is_get:
            step+=1
            add_num=num_reverse(add_num)+add_num
            is_get=check(add_num)
        if step <= 8:
            return ('经过%d步得到回文数:%d' % (step, add_num))
        return 0
    else:
        return ('输入数字不符合规范，请重试!')


print(get_steps(check))


