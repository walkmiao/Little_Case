#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 双向链表.py
# @Author: lch
# @Date  : 2018/11/29
# @Desc  :


class Node:
    def __init__(self, data):
        self.data = data
        self._pre = None
        self._next = None

    def __str__(self):
        return '{}({},{},{})'.format(self.__class__.__name__, self._pre, self._next, self.data)


class DoubleChain:
    def __init__(self):
        self.head = None

    def append(self, data):
        append_node = Node(data)
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node:
                if node._next:
                    node = node._next
                else:
                    break
            node._next = append_node
            append_node._pre = node
    def __str__(self):
        chain_list =[]
        node = self.head
        while node:
            chain_list.append(node)
            if node._next:
                node = node._next
            else:
                break
        if chain_list:
            return 'DoubleChain:{}'.format('-->'.join(str(i) for i in chain_list))
        else:
            return 'DoubleChain:None'


dh = DoubleChain()
dh.append(1)
dh.append(2)
print(dh)




