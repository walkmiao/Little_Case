#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 深浅拷贝.py
# @Author: lch
# @Date  : 2018/5/22
# @Desc  :
import copy
'''
对象赋值
'''
print('对象赋值'.center(20,'*'))
a=['spe','earth',['puck','lucifer']]
print('a内存地址:%s'%(id(a)))
print([id(i) for i in a])

b=a
print(a is b)
print('b内存地址:%s'%(id(b)))
print([id(i) for i in b])
a[0]='foot' #a[0]是不可变对象，更改a[0]内存地址也会变化
a[2].append('dog')
print('----------------')
print([id(i) for i in a])
print([id(i) for i in b])
'''
浅拷贝
'''
print('浅拷贝'.center(20,'*'))
a=['spe','earth',['puck','lucifer']]
print('a内存地址:%s'%(id(a)))
print([id(i) for i in a])

b=copy.copy(a) #浅拷贝会生成一个新的对象，但是对对象中的元素只会使用原始元素的内存地址
print('b内存地址:%s'%(id(b)))
print([id(i) for i in b])
a[0]='foot' #a[0]是不可变对象，更改a[0]内存地址也会变化
a[2].append('dog')
print('----------------')
print([id(i) for i in a])#由于list的第一个元素是不可变类型，所以will对应的list的第一个元素会使用一个新的对象。
# 但是list的第三个元素是一个可变类型，修改操作不会产生新的对象，所以will的修改结果会相应的反应到wilber上
print([id(i) for i in b])

'''
深拷贝
'''
print('深拷贝'.center(20,'*'))
a=['spe','earth',['puck','lucifer']]
print('a内存地址:%s'%(id(a)))
print([id(i) for i in a])

b=copy.deepcopy(a)
print('b内存地址:%s'%(id(b)))
print([id(i) for i in b])
a[0]='foot' #a[0]是不可变对象，更改a[0]内存地址也会变化
a[2].append('dog')
print('----------------')
print([id(i) for i in a])
print([id(i) for i in b])
'''
其实，对于拷贝有一些特殊情况：

对于非容器类型（如数字、字符串、和其他’原子’类型的对象）没有拷贝这一说
也就是说，对于这些类型，”obj is copy.copy(obj)” 、”obj is copy.deepcopy(obj)”

如果元祖变量只包含原子类型对象，则不能深拷贝，看下面的例子
'''