#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 19:05
# @Author  : lch
# @File    : __new__方法.py
'''
new方法的作用是定制类的实例，init方法则是在new方法生成实例后，对实例的初始化 也即new在前 init在后
重写new方法必须有返回值 返回的也就是生成的实例，init方法则不用返回值
super(param1,param2) param1,param2可以是类,对象 也可以是类，类
def super(cls,inst):
    mro=inst.__class__.mro()
    return mro[mro.index(cls)+1]

def super(cls1,cls2):
    mro=cls2.mro()
    return mro[mro.index(cls)+1]
'''
class A(): #python3中默认继承object
    def __new__(cls, *args, **kwargs):
        ins=super(A, cls).__new__(cls, *args, **kwargs) #按照上面super的解释，所以这里super(A,cls)相当于是object
        print('cls mro list:%s'%(cls.mro()))
        print('A instance is newed:%s'%ins)
        return ins
    def __init__(self):
        print('current instance is %s'%self)
        super(A, self).__init__() #此处super(A,self)也是object
        print('instance inited!')

a=A()


