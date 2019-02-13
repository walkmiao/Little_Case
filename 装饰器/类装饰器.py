#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 类装饰器.py
# @Author: lch
# @Date  : 2018/7/2
# @Desc  :
import time

class Decorator():
    def __init__(self, para):
        self.para = para

    def __call__(self, func):
        self.func = func

        def decorator(*args, **kwargs):
            start = time.time()
            print('%s start %s' % (self.func.__name__, self.para))
            result = self.func(*args, **kwargs)
            print('%s 执行完毕,共耗时%s' %(self.func.__name__, time.time()-start))
            return result
        return decorator


@Decorator('excute')
def do_something(*args):
    time.sleep(5)
    print('do something')

print(do_something(*range(100000)))