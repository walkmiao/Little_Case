#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : __getattr__.py
# @Author: lch
# @Date  : 2018/5/21
# @Desc  :

class MyDict(dict):
    def __init__(self,**kw):
        super(MyDict, self).__init__(**kw)
    # def __getattr__(self, k):
    #     try:
    #         return self[k]
    #     except KeyError:
    #         raise AttributeError('%s has no Attribute %s'%(self.__class__,k))
    # def __setattr__(self, key, value):
    #     self[key]=value

# d=MyDict(a=1,b='go')
# print(d.a)
c={'a':1,'b':2}
b= 'a' in c
print( 'a' in c)