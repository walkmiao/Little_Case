#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/28 9:48
# @Author  : LCH
# @Site    : 
# @File    : 元类.py
# @Software: PyCharm

#使用type方法创建类

def f(self,name):
    self.name=name
def get_f(self):
    return self.name
My=type('Myname',(object,),dict(__init__=f,get_name=get_f))
m=My('lch')
print(m.get_name())
print(type(m))

#元类的简单实用
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list, metaclass=ListMetaclass):
   pass
m=MyList()
m.add('ls')
print(m)
print(m.__dict__)
