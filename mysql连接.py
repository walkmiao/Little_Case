#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 15:31
# @Author  : LCH
# @Site    : 
# @File    : mysql连接.py
# @Software: PyCharm
import mysql.connector
con=mysql.connector.connect(user='root',password='5231811',database='test')
curson=con.cursor()
curson.execute('create table student(id varchar (20) primary key ,name varchar (20))')
con.commit()
curson.close()