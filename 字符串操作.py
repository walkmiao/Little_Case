#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/24 22:11
# @Author  : lch
# @File    : 字符串操作.py
#利用字符串切片来使字符串两边的空格消除,非常简洁的代码就能使这个功能实现
def trim(s):
    while s[:1] == ' ':
        s = s[1:]

    while s[-1:] == ' ':
        s = s[:-1]

    return s
if trim('hello  ') != 'hello':
    print('测试失败at1!')
elif trim('  hello') != 'hello':
    print('测试失败at2!')
elif trim('  hello  ') != 'hello':
    print('测试失败at3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败at4!')
elif trim('') != '':
    print('测试失败at5!')
elif trim('    ') != '':
    print('测试失败at6!')
else:
    print('测试成功!')
