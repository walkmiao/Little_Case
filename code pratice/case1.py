#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : case1.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :

import os

def print_directory_contents(sPath):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    for i in os.listdir(sPath):
        new_path=os.path.join(sPath,i)
        if os.path.isfile(new_path):
            print(new_path)
        else:
            print_directory_contents(new_path)

print_directory_contents('/Users/lch/PycharmProjects/')
