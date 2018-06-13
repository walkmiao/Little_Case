#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : classmethod.py
# @Author: lch
# @Date  : 2018/5/18
# @Desc  :



class Kls(object):
    def __init__(self, data):
        self.data = data

    def printd(self):    #普通方法
        print(self.data)

    @staticmethod        #静态方法
    def smethod(*arg):
        print('Static:', arg)

    @classmethod        #类方法
    def cmethod(*arg):
        print('Class:', arg)

'''
下面的打印结果最能说明问题

# >> > ik = Kls(23)
# >> > ik.printd()
# 23
# >> > ik.smethod()  实例能够调用静态方法
# Static: ()

# >> > ik.cmethod()  实例能都调用类方法，但第一个参数传进去的不是实例自己，而是类
# Class: (<class '__main__.Kls'>, )

# >> > Kls.printd()  类自己不能调用普通方法，必须实例化对象后来调用，类无法把实例参数self传进去
# TypeError: unbound method printd() must be called with Kls instance as first argument (got nothing instead)

# >> > Kls.smethod()类可以调用静态方法，静态方法默认不传类或实例参数，而是实实在在的参数
# Static: ()

#         >> > Kls.cmethod() 类当然也可以调用类方法，方法的第一个参数也是类。其实类也是一种对象。不过是能创造对象的对象！
# Class: (< class '__main__.Kls' >,)
'''
