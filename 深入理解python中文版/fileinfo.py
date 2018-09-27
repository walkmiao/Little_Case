#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : fileinfo.py
# @Author: lch
# @Date  : 2018/8/17
# @Desc  :
class UserDict(dict):
    def __init__(self,username):
        super(UserDict, self).__init__()
        self['name'] = username
class FileInfo(UserDict):
    def __init__(self,username):
        super(FileInfo, self).__init__(username)

f = FileInfo('lucas')
print(f)