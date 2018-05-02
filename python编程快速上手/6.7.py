#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 15:17
# @Author  : LCH
# @Site    : 
# @File    : 6.7.py
# @Software: PyCharm
def printTable(str_list):
    num_list=[]
    for i in str_list:
        num=0
        for j in i:
            if len(j)>num:
                num=len(j)
        num_list.append(num)
    for i in range(len(str_list[0])):
        for j in range(len(num_list)):
            print('%s '%(str_list[j][i].rjust(num_list[j])),end='')
        print('\n')






tableData=[['applessss','oranges','cherries','banana'],
           ['Alice4444','Bob','Carol','David'],
           ['dogs','catssss','moose','goose'],
           ['i','am','a','joker']
           ]
printTable(tableData)
# print(len(tableData),len(tableData[0]))