#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 15:16
# @Author  : LCH
# @Site    : 
# @File    : 5.6.2.py
# @Software: PyCharm
def displayInventory(dic):
    print('Inventory:')
    sum=0
    for k,v in dic.items():
        print('%d %s'%(v,k))
        sum=sum+v
    print('Total number of items:%d'%sum)

def addToInventory(inventory,addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i]+=1
    return inventory

inv={'gold coin':42,'rope':1}
drangonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv=addToInventory(inv,drangonLoot)
displayInventory(inv)