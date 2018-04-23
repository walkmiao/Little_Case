#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 14:22
# @Author  : LCH
# @Site    : 
# @File    : 文件操作.py
# @Software: PyCharm
import os
# #输出系统环境变量 是个dict
# print(os.environ['path'])
# print(os.environ.get('path'))
# #输出绝对路径
# print(os.path.abspath('.'))
# #合成路径
# print(os.path.join('/user/fire','os.txt'))
# #创建删除目录
# os.mkdir('./test')
# os.rmdir('./test')
# #拆分路径
# print(os.path.split('/user/fire/os.txt'))
# #获取文件扩展名
# print(os.path.splitext('/user/fire/os.txt'))

#编写一个程序，能在指定目录下查找文件名包含指定字符串的文件，并打印出相对路径。
class findStr():
    def __init__(self,path):
        self.path=path
        self.file_list=[]
        self.str_list=[]
    def get_filepath(self,path):
        if os.path.isdir(path):
            for i in os.listdir(path):
                if os.path.isdir(os.path.join(path,i))==False:
                    self.file_list.append(os.path.join(path,i))
                else:
                    self.get_filepath(os.path.join(path,i))
        else:
            self.file_list.append(path)
        return self.file_list


    def find_str(self,anystr,file_list):
        for i in file_list:
            if anystr in i:
                self.str_list.append(i)
        return self.str_list
    def main(self,anystr):
        self.file_list=self.get_filepath(self.path)
        self.str_list=self.find_str(anystr,self.file_list)
        for i in self.str_list:
            print(i)
f=findStr('.')
if __name__=='__main__':
    # print(f.get_filepath(f.path))
    # print(f.find_str('config',f.get_filepath(f.path)))
    f.main('.py')
# print(get_filepath('.'))
# print([os.path.abspath(i) for i in os.listdir('D:\PycharmProjects\Little_Case\.idea')])




