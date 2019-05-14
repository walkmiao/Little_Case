#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 双向链表.py
# @Author: lch
# @Date  : 2019/3/13
# @Desc  :

import copy


class Node:
    def __init__(self, val):
        self.val = val
        self._next = None

    def __repr__(self):
        return 'Node(val={val}, next={next})'.format(val=self.val, next=self._next)


class Link:
    def __init__(self):
        self._root = Node("ROOT")

    def insert(self, node, index):  # node的插入
        if index <= 0:
            print("[IndexError] index must >= 1")

        root_node = self._root
        count = 0
        while root_node:
            if root_node._next:
                count += 1
                if index == count:
                    tag_node = root_node._next
                    root_node._next = node
                    node._next = tag_node
                    break
                else:
                    root_node = root_node._next
                    continue
            else:
                print(f"LINK最大长度为{count},index:{index}")
                break

    def append(self, node):  # node的末尾添加
        root_node = self._root
        while root_node:
            if root_node._next:
                root_node = root_node._next
            else:
                root_node._next = node
                break

    def reverse(self):  # 链表转置
        link_list = []
        root_node = self._root
        while root_node:
            if root_node._next:
                link_list.append(root_node._next)
                root_node = root_node._next
            else:
                break

        root_node_2 = self._root
        for node in link_list[::-1]:
            node._next = None
            root_node_2._next = node
            root_node_2 = node

    def get_last_node(self):  # 获取最后的节点
        root_node = self._root
        while root_node:
            if root_node._next:
                root_node = root_node._next
            else:
                return root_node

    def remove(self, item): # 移除节点值为item的节点
        root_node = self._root
        while root_node:
            next_node = root_node._next
            if next_node:
                if next_node.val == item:
                    if next_node._next:
                        root_node._next = next_node._next
                    else:
                        root_node._next = None
                    break
                root_node = next_node

            else:
                return "不存在Node({})节点".format(item)

    def __iter__(self):
        root_node = self._root
        while root_node:
            yield root_node
            if root_node._next:
                root_node = root_node._next
            else:
                break

    def link_show(self):
        root_node = self._root
        output = str(root_node.val) + " -> "
        while root_node:
            if root_node._next:
                if root_node._next._next:
                    output = output + str(root_node._next.val) + " -> "
                else:
                    output = output + str(root_node._next.val)
                root_node = root_node._next
            else:
                return output



link_list = Link()
for i in range(1, 11):
    link_list.append(Node(i))
print(link_list.link_show())
link_list.insert(Node(22),3)
print(link_list.link_show())
link_list.insert(Node(29),5)
print(link_list.link_show())
link_list.reverse()
print(link_list.link_show())
print(link_list.get_last_node())
print(link_list.remove(10))
print(link_list.link_show())

