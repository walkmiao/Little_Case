#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : search方法.py
# @Author: lch
# @Date  : 2018/5/30
# @Desc  :
import re

'''
search方法
'''
phonenum = 'my phone number is 425-999-0845.'

# （）设置分组,括号在正则中有特殊的含义，如果本身文本带括号需要用\进行转义
phoneregex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

# search 方法返回match对象，match对象的group方法返回匹配的文本
match = phoneregex.search(phonenum)
if match:
    print(match)
    print(match.groups())  # ('425', '999-0845')
    print(match.group())  # 425-999-0845
    print(match.group(1))  # 425
    print(match.group(2))  # 999-0845

# 管道|在匹配多个表达式时很有用
pipregex = re.compile(r'Bat(number|view|home)')
match = pipregex.search('Bathome is new')
if match:
    print(match.groups())
    print(match.group())


'''
贪心和非贪心匹配
'''
regex1=re.compile(r'(ha){3,5}')
regex2=re.compile(r'(ha){3,5}?')#?在正则中的作用一个是匹配分组0或1次，还有一个就是非贪婪匹配
match1=regex1.search('hahahahaha')
match2=regex2.search('hahahahaha')
print(match1.group())
print(match1.group(1))
print(match2.group())

'''
findall方法返回所有匹配的文本,返回的是一个列表
'''
s='work:455-629-5576 home:256-338-9789'
regex=re.compile(r'\d{3}-\d{3}-\d{4}')
flist=regex.findall(s)
print(flist)
#如果表达式有分组的话，则会返回元祖的列表
regex=re.compile(r'(\d{3})-\d{3}-(\d{4})')
flist=regex.findall(s)
match=regex.search(s)
print(flist)
print(match.group())

'''
^和$匹配开始和结束,如果同时使用这两个 则整个字符串必须完整匹配 匹配一部分是不行的
'''
regex=re.compile(r'^\d+$') #表明以数字开始 以数字结束
m=regex.search('1234567')
print(m.group())
m1=regex.search('123 456')
print(m1)

'''
.匹配除换行外任何字符，re.DOTALL作为re.compile()的第二个参数 可以让.匹配任何字符
re.I 则是忽略大小写
'''
s='abc@123 \n123'
regex=re.compile(r'.*')
regex2=re.compile(r'.*',re.DOTALL)
print(regex.search(s).group())
print(regex2.search(s).group())