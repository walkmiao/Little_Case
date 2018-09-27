#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 链表.py
# @Author: lch
# @Date  : 2018/8/22
# @Desc  :
'''
数据结构之链表
'''


class Node:
    def __init__(self, data, p_next=None):
        self.data = data
        self._next = p_next

    def __repr__(self):
        return '%s:%s'.format(self.data, __class__)


class ChainTable:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length==0

    def append(self, data_or_node):
        if isinstance(data_or_node, Node):
            item = data_or_node
        else:
            item = Node(data_or_node)
        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.is_empty():
            print('[err] chain table is empty!')
        if index<0 or index>self.length:
            print('[err] chain table out of range! ')






