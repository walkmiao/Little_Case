#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 单例实现.py
# @Author: lch
# @Date  : 2018/10/11
# @Desc  :

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_ins'):
            cls._ins = super(Singleton, cls).__new__(cls)  # 这里object的new不需要传参 注意！！！！

        return cls._ins

    def __init__(self, name):
        self.name = name
        print('self is {}'.format(self))

    def __repr__(self):
        return "{}:{}".format(self.__class__.__name__, self.name)


p1 = Singleton('p1')
p2 = Singleton('p2')
print('p1==p2:%s' %(p1 is p2))
print(p1, p2)

# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         print('cls is {}'.format(cls))
#         if not hasattr(cls, '_ins'):
#             cls._ins = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._ins
#
#     def __init__(self):
#         print('self is {}'.format(self))
#
#     def __repr__(self):
#         return "{}".format(self.__class__.__name__)
#
#
# p1 = Singleton()
# p2 = Singleton()
# print('p1==p2:%s' %(p1 is p2))
# print(p1, p2)
