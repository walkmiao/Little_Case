#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 20:28
# @Author  : LCH
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import xlrd
import xlwt,re
from openpyxl import Workbook

def get_name(path,value,pre):
    result={}
    wb = xlrd.open_workbook(path)
    sheet = wb.sheets()[0]
    rows = sheet.nrows
    for i in value:
        for j in range(1,rows):
            row_value = sheet.row_values(j)
            if row_value[3] == i:
                result[('W3.'+pre+'.'+i)]=row_value[5]
    return result


source_wb = xlrd.open_workbook('./query/YX.xls')
source_sheet=source_wb.sheets()[0]
value = source_sheet.col_values(1)
regex = re.compile(r'W3.(\w+).(\w+)', re.DOTALL)
dic=dict()
for i in value[1:]:
    match = regex.match(i)
    book_name = match.group(1)
    node_name = match.group(2)
    dic.setdefault(book_name,[]).append(node_name)
my = []
for i,j in dic.items():
    if i=='UNIT1':
        d=get_name(('./query/'+i+'.xls'),j,i)
        my.append(d)
    elif i=='FGD':
        d = get_name(('./query/' + i + '.xls'), j,i)
        my.append(d)
    elif i=='UNIT2':
        d = get_name(('./query/' + i + '.xls'), j,i)
        my.append(d)
workbook = Workbook()  # 创建表
ws = workbook.active  # 创建表sheet
ws.append([ 'name', 'ptname', ])  # 添加表头
for i in my:
    for key,value in i.items():
        line=[key,value]
        ws.append(line)
workbook.save('test2.xls')

