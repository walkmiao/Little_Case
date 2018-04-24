#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 19:31
# @Author  : lch
# @File    : 正则表达式.py
import re
#返回一个pattern对象
pattern=re.compile(r'\d{3}-\d{8}')
#返回一个match对象
match=pattern.match('025-848053533')
match_2=re.match(r'\d{3}-\d{8}','025-84805353')
if match:
    #获取分组信息
    print(match.group())
    #获取匹配时使用的文本
    print(match.string)
    #获取pattern对象
    print(match.re)
    #正则表达式开始的索引
    print(match.pos)
    # 正则表达式结束的索引
    print(match.endpos)
    print(match.lastgroup)

p = re.compile(r'\w+@\w+.com')
s="""xiasd@163.com, sdlfkj@.com sdflkj@180.com solodfdsf@123.com sdlfjxiaori@139.com saldkfj.com oisdfo@.sodf.com.com"""
print(p.findall(s))


