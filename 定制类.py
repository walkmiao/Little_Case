#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 19:44
# @Author  : LCH
# @Site    : 
# @File    : 定制类.py
# @Software: PyCharm

'''
如果一个类想被用于for in 循环，那它需要在内部实现__iter__方法，该方法返回一个
可迭代对象，并调用类的__next__方法不断迭代
'''
class Fib():
    def __init__(self):
        self.a=0
        self.b=1
        self.n=0
    def __iter__(self):
        return self
    # def __next__(self):
    #     self.a,self.b=self.b,(self.a+self.b)
    #     if self.n<10:
    #         self.n+=1
    #         return self.a
    #     raise StopIteration
    def __getitem__(self, item):
        a,b=1,1
        for x in range(item):
            a,b=b,a+b
        return a

f=Fib()
print(f[4])
# for i in f:
#     print(i)

