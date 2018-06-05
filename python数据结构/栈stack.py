#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 栈stack.py
# @Author: lch
# @Date  : 2018/6/5
# @Desc  :
'''
Stack()    建立一个空的栈对象
push()     把一个元素添加到栈的最顶层
pop()      删除栈最顶层的元素，并返回这个元素
peek()     返回最顶层的元素，并不删除它
isEmpty()  判断栈是否为空
size()     返回栈中元素的个数
getmin()   获取栈中最小值
'''
import logging

class Node():
    def __init__(self,n):
        self.value = n
        self.next = None

class Stack():
    global count
    count = 0

    def __init__(self):
        self.top = None

    def push(self,n):
        global count
        node = Node(n)
        node.next = self.top
        self.top = node
        count +=1
        logging.warning('Insert %s to stack!'%n)

    def pop(self):
        global count
        count -=1
        value = self.top.value
        self.top = self.top.next
        logging.warning('Get %s from stack!'%value)
        return value

    def peek(self):
        if self.top.value:
            logging.warning('peek value of Stack is %s' % self.top.value)
            return self.top.value
        else:
            return

    def isEmpty(self):
        if self.top:
            logging.warning('Stack is not Empty!')
            return
        else:
            logging.warning('Stack is  Empty!')
            return True

    def size(self):
        global count
        logging.warning('count is %s'%count)
        return count
    def getmin(self):
        pass

s = Stack()
s.push(2)
s.push(3)
s.pop()
s.push(78)
s.push(22)
s.peek()
s.pop()
s.isEmpty()
s.pop()
s.pop()
s.isEmpty()

s.push(12)
for i in range(10):
    s.push(i)

s.size()