#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 2.1.py
# @Author: lch
# @Date  : 2018/8/16
# @Desc  :
import sys

def build_connect_string(param):
    '''

    :param param:database dict
    :return:join database param and ';'
    '''
    lambda_func =lambda s:s

    if lambda_func(param):
        return ';'.join([k+'='+v for k, v in param.items()])
    else:
        return


if __name__ == '__main__':
    myParams = {
        "server": "game",\
        "database": "master",
        "uid": "sa",
        "pwd": "secret"
    }
    print(build_connect_string(myParams))
    print(dir(build_connect_string))
else:
    print('%s module is imported succ~' % __name__)
