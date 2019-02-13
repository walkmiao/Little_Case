#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 9:14
# @Author  : LCH
# @Site    : 
# @File    : 东北公司vestore分割excel.py
# @Software: PyCharm
import xlrd, re, json
from openpyxl import Workbook
from multiprocessing import Pool


def find_nodes(source_wb, target_wb, reg=None):
    ws = target_wb.active  # 创建表sheet
    source_sheet = source_wb.sheets()[0]
    source_title = source_sheet.row_values(0)
    ws.append(source_title)
    source_info = source_sheet.col_values(12)[1:]
    for key, value in enumerate(source_info):
        if reg.match(value):
            row_value = source_sheet.row_values(key+1)
            ws.append(row_value)
    target_wb.save('DB-YX.xlsx')




    # # 将合法的点生成符合配置要求的excel
    # for i in range(len(valid_node)):
    #     line = [i, valid_node[i], invalid, coef, base]
    #     ws.append(line)
    # workbook.save(file + '.xlsx')
    #
    # not_find['未找到点名数'] = len(not_find)
    # not_find['有效点名总数'] = len(all_node)
    # with open(file, 'w') as f:
    #         f.write(json.dumps(not_find, ensure_ascii=False))


if __name__ == '__main__':
    source_wb = xlrd.open_workbook('./query/AllLabInfomation.xls')
    target_wb = Workbook()
    regex = re.compile(r'.+(状态|门)$')  # 筛选合法点名的正则
    find_nodes(source_wb,target_wb,regex)
    # test = '白城电厂#1号机#1稀释风机运行状态'
    # if regex.match(test):
    #     print('ok')
    # print(regex.match(test))