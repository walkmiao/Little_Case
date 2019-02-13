#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : print_object_method.py
# @Author: lch
# @Date  : 2018/8/16
# @Desc  :
def info(object, collase=1, space=10):
    method_list = [method for method in dir(object) if callable(getattr(object, method))]
    process_func = lambda s:' '.join(s.split()) if collase else s
    print('\n'.join(['%s %s' % (method.ljust(space), process_func(str(getattr(object, method).__doc__))) for method in method_list]))
if __name__ == '__main__':
    info([],collase=1,space=20)
