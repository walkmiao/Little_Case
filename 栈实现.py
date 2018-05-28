#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: lch
# @Date  : 2018/5/16
# @Desc  :

class Node():
    '''
    定义Node类，包含栈存放的值value，以及下一个元素的位置和值next
    当出栈后需要把next这个指针变成栈顶
    '''
    def __init__(self,value):
        self.value=value
        self.next=None   #初始化下个next指针为空

class Mystack():
    '''
    定义栈类，实现取栈顶的peek方法，
    入栈的push方法，出栈的pop方法。
    并考虑元素出栈后栈顶的指针变化
    '''
    def __init__(self):
        self.top=Node   #初始化栈顶元素为空

    def peek(self):
        if self.top:
            print('get top value %s '%self.top.value)
            return self.top.value
        else:
            return None
    def push(self,value):
        node=Node(value)
        node.next=self.top  #self.top=顶端位置+顶端值，赋值给node后 node=（顶端元素位置，值）+当前插入的值
        self.top=node       #新的top=（顶端元素位置，值）+当前插入的值
        print('insert %s'%value)

    def pop(self):
        if self.top:
            tmp=self.top.value
            self.top=self.top.next
            print('get %s out'%tmp)
            return tmp
        else:
            return None

if __name__=='__main__':
    stack=Mystack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.push(20)
    stack.push(1)
    stack.pop()
    stack.peek()
