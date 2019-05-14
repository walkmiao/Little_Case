#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 第九章-利用装饰器检查函数的参数类型.py
# @Author: lch
# @Date  : 2019/2/20
# @Desc  :


def type_check(*args):
    def decorator(func):
        def wrap(*args_2, **kw):
            if len(args)!=len(args_2) + len(kw):
                raise BaseException('参数类型不匹配')
            para_list = list(args_2) + list(kw.values())
            for no, p in enumerate(para_list):
                assert type(p) == args[no], f'{p} is not {args[no]} type'
            return func(*args_2, **kw)
        return wrap
    return decorator


@type_check(int, int)
def check_test(x, y):
    return x+y


print(check_test(x=1, y=2))