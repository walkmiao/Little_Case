#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 13:18
# @Author  : LCH
# @Site    : 
# @File    : 闭包.py
# @Software: PyCharm

#写一个闭包，返回一个函数
def lazy_sum(*args):
    def sum():
        r=0
        for i in args:
            r+=i
        return r
    return sum
print(lazy_sum(*range(10))) #返回一个函数，但是没有执行,加*是因为函数参数为可变参数，*可以把range(10)转换为可变参数
print(lazy_sum(*range(10))())#这次执行了

#使用了闭包后，返回的函数引用了变量i 返回函数并非立刻执行而是等到全部都返回后才执行，这时i已经为3 所以结构都是9
def closure():
    f=[]
    for i in range(1,4):
        def result():
            return i*i
        f.append(result)
    return f
f1,f2,f3=closure()
print(f1(),f2(),f3())

'''这是更完整的类比，下面列出了各个情况 可以参照代码仔细思考一下为什么
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f())    # 列表中的元素为f()的返回值，即int型数据
    return fs    # 返回值为列表

a = count()
print(a)

def count1():
    # fs = []
    for i in range(1, 4):
        def f():
             return i*i
        # fs.append(f())
    return f    # 返回值为function类型，for循环里相互覆盖，因此只返回最后一次的函数对象

a = count1()
print(a)
print(a())

def count2():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i    # 引用了外部变量i，但并非立即执行，直到调用f()时才执行，此时i的值已经都变了
        fs.append(f)    # 列表中的元素为function类型，返回for循环的三个元素
    return fs    # 返回值为列表

a = count2()
print(a)
for n in a:
    print(n())

def count3():
    def g(j):
        def f():
            return j * j    # 这里每次f()在调用时，其引用的外部变量j已经确定了
        return f
    fs = []

    for i in range(1, 4):
        fs.append(g(i))    # 列表中的元素为function类型，返回for循环的三个元素
    return fs    # 返回值为列表

a = count3()
print(a)
for n in a:
    print(n())

def createCounter():
    L = [0]    # 列表L的内存地址在初次调用时已经给定，且L[0]即第一个元素指向整数0
    def counter():
        L[0] += 1    # 改变列表L中第一个元素的值，但并没有改变列表L的内存地址
        return L[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



