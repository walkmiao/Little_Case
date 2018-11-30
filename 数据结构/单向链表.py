#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 链表.py
# @Author: lch
# @Date  : 2018/8/22
# @Desc  :
'''
数据结构之链表
'''

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, data):
        self._next = None
        self.data = data

    def __str__(self):
        return '{node}({data})'.format(node=self.__class__.__name__, data=self.data, next=self._next)

    def __repr__(self):
        return '{node}({data})'.format(node=self.__class__.__name__, data=self.data, next=self._next)



class Chain:
    def __init__(self):
        self.head = None

    def append(self, data):
        '''
        尾部追加节点
        :param data: 节点数据
        :return:
        '''
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            next = self.head
            while next._next:
                next = next._next
            next._next = node
        logger.debug(self)

    def get_node(self, index):
        '''
        获取指定节点
        :param index: 节点位置
        :return: Node
        '''
        index = index if index >= 0 else len(self) + index
        if index > len(self) -1 or index < 0:
            raise Exception("node index is not exist!")
        node = self.head
        while index:
            node = node._next
            index -= 1
        logger.debug('you get_node {}'.format(node))
        return node

    def del_node(self, index):
        '''
        删除指定节点
        :param index: 节点位置
        :return:
        '''
        index = index if index >= 0 else len(self) + index
        if index > len(self) -1 or index < 0:
            raise Exception("del index is no exist!")
        node = self.head
        if index == 0:
            self.head = self.head._next if self.head._next else None
        else:
            index = index - 1
            while index:
                node = node._next
                index -= 1
            node_next = node._next
            node_next_next = node_next._next
            node._next = node_next_next

        logger.debug(self)

    def insert_node(self, data, index):
        '''
        在指定顺序插入节点
        :param data: 节点数据
        :param index: 节点位置
        :return:
        '''
        node_inert = Node(data)
        index = index if index >= 0 else len(self) + index
        if index > len(self) - 1 or index < 0:
            raise Exception("insert index is no exist!")
        node = self.head
        if index == 0:
            node_inert._next = self.head
            self.head = node_inert

        else:
            index = index -1
            while index:
                node = node._next
                index -= 1
            pre_node = node
            next_node = node._next
            pre_node._next = node_inert
            node_inert._next = next_node
        logger.debug(self)

    def set_node(self, data, index):
        '''
        重新设置节点数据
        :param data: 节点数据
        :param index: 节点位置
        :return:
        '''
        index = index if index >= 0 else len(self) + index
        if index > len(self) - 1 or index < 0:
            raise Exception("insert index is no exist!")
        node = self.head
        if node:
            if index == 0:
                self.head.data = data
            else:
                while index and node:
                    node = node._next
                    index -= 1
                node.data = data

        else:
            raise Exception("Current Chain is empty!")
        logger.debug('set_node执行后 Chain={}'.format(self))

    def reverse(self):
        '''
        链表反转
        :return:
        '''
        if len(self) > 0:
            if len(self) == 1:
                pass
            else:
                reverse_count = len(self) - 1
                cache_chain = Chain()
                head_node = cache_chain.head = self.get_node(-1)
                while reverse_count > 0:
                    tmp = self.get_node(-2)
                    tmp._next = None
                    head_node._next = tmp
                    head_node = head_node._next
                    reverse_count -= 1
                self.head = cache_chain.head
        else:
            pass

    def __len__(self):
        '''
        获取链表长度
        :return: 链表长度
        '''
        length = 0
        node = self.head
        while node:
            length += 1
            if node._next:
                node = node._next
            else:
                break
        return length

    def travel_nodes(self):
        '''
        遍历链表
        :return:
        '''
        node = self.head
        while node:
            print(str(node) + '↓')
            node = node._next

    def __str__(self):
        chain_list = []
        node = self.head
        while node:
            chain_list.append(node)
            node = node._next
        if chain_list:
            return 'Chain:' + '-->'.join(str(node) for node in chain_list)
        else:
            return 'Chain:no node in Chain'

    def __repr__(self):
        return self.__str__()


chain = Chain()
chain.append('a')
chain.append('b')
chain.append('c')
chain.get_node(-1)
chain.insert_node('I', 2)
chain.insert_node('s',2)
chain.del_node(2)
chain.reverse()
print(chain)
chain.set_node('sb', 2)
chain.insert_node('nobb', 1)
print(len(chain))
chain.travel_nodes()












