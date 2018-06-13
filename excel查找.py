#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 10:35
# @Author  : LCH
# @Site    : 
# @File    : excel查找.py
# @Software: PyCharm
import xlrd, re, json
from openpyxl import Workbook


def find_nodes(source_wb, reg, file, *new_wb):
    pre = 'W3.'
    invalid = 0
    coef = 1
    base = 0
    workbook = Workbook()  # 创建表
    ws = workbook.active  # 创建表sheet
    ws.append(['ptorder', 'ptname', 'invalid', 'coef', 'base'])  # 添加表头
    source_sheet = source_wb.sheets()[0]
    source_node = source_sheet.col_values(3)  # 老sis转发表里的点名列表
    not_find = dict()  # 在新sis里没有找到的点名
    new_node = []  # 新sis所有表的点
    valid_node = []  # 在新sis表里能找的点
    all_node = []  # 筛选合法点去除空，无

    # 将新sis里的五个表中的点名汇总成一个列表
    for wb in new_wb:
        sheet = wb.sheets()[0]
        new_node += sheet.col_values(3)

    for i in source_node:
        if reg.match(i):  # 判断老sis点名是否符合寻找要求，去掉无与空白
            all_node.append(i)
            if i in new_node:  # 判断老sis里的点是否在新sis的点名列表中
                idx = new_node.index(i)
                if 0 <= idx < 14054:  # 判断找到的点存在新sis的哪张表中，加上点的前缀
                    i = pre + 'UNIT1.' + i
                elif 14054 <= idx < 26145:
                    i = pre + 'UNIT2.' + i
                elif 26145 <= idx < 28077:
                    i = pre + 'SM.' + i
                elif 28077 <= idx < 35608:
                    i = pre + 'FW.' + i
                else:
                    i = pre + 'FGD.' + i
                valid_node.append(i)  # 给找到的点加上前缀后存入列表
            else:
                squ = source_node.index(i)+1  # 如果没有找到,取出点名所对应的序号
                not_find[squ] = i  # 存入字典

    # 将合法的点生成符合配置要求的excel
    for i in range(len(valid_node)):
        line = [i, valid_node[i], invalid, coef, base]
        ws.append(line)
    workbook.save(file + '.xlsx')

    not_find['未找到点名数'] = len(not_find)
    not_find['有效点名总数'] = len(all_node)
    with open(file, 'w') as f:
            f.write(json.dumps(not_find, ensure_ascii=False))


if __name__ == '__main__':
    source_wb = xlrd.open_workbook('./query/1.xls')
    source_wb2 = xlrd.open_workbook('./query/2.xls')
    new_wb1 = xlrd.open_workbook('./query/UNIT1.xls')
    new_wb2 = xlrd.open_workbook('./query/UNIT2.xls')
    new_wb3 = xlrd.open_workbook('./query/SM.xls')
    new_wb4 = xlrd.open_workbook('./query/FW.xls')
    new_wb5 = xlrd.open_workbook('./query/FGD.xls')
    regex = re.compile(r'[a-zA-Z0-9]+\w+[a-zA-Z0-9]*')  # 筛选合法点名的正则
    find_nodes(source_wb, regex, '1号机组.txt', *(new_wb1,new_wb2,new_wb3,new_wb4,new_wb5))
    find_nodes(source_wb2, regex, '2号机组.txt', *(new_wb1, new_wb2, new_wb3, new_wb4, new_wb5))

