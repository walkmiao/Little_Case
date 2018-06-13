#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 22:49
# @Author  : lch
# @File    : 元类中__call__的作用.py
'''
元类是一种能生产出类的类，可以把类看作是元类的一个实例。所以说类其实也是一个对象。元类是类的模板必须从type继承

'''
class MyMetaClass(type):
    def __new__(cls, name, bases, dic): #此处cls是元类本身即MyMetaClass,name是创造的类的类名，bases是要创造的类的父类集合，dic则是创造的类的方法集合
        print('Metaclass new called')
        print('cls:%s name:%s \n bases:%s dic:%s ' % (cls, name, bases, dic))
        dic['setname']=lambda self, name: 'hello '+name #在元类中动态添加setname方法,由元类创造出的类将会拥有此方法
        return super(MyMetaClass, cls).__new__(cls, name, bases, dic)
    def __call__(self, *args, **kwargs): #此处的self即创造的类
        '''
        如果在元类中实现了call方法，那么类的实例化不会调用new方法而是调用元类的call方法，
        也即Test的new和init方法被call拦截了，如果call方法中没有实现对Test的new方法和init方法的调用的话,那么将不会产生Test对象。
        而且必须要返回Test对象即i
        '''
        print('Metaclass call called')
        print(self)
        i=self.__new__(self,*args,**kwargs) #此处调用创造的类即Test的new方法
        print(i)
        i.__init__()#此处调用Test实例的init方法
        return i#返回Test实例

class Test(object,metaclass=MyMetaClass):
    def __new__(cls, *args, **kwargs):
        print('Test new called..')
        return super(Test, cls).__new__(cls,*args,**kwargs)
    def __init__(self):
        print('Test init called')
    def getname(self,name):
        print(name)

a=Test()
print(a)
a.getname('lch')
print(a.setname('lch')) #此处a拥有setname方法