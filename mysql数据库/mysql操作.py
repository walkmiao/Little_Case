#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mysql操作.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :
import mysql.connector as con

conn=con.connect(user='root',password='zaq12wsx',database='test')
curson=conn.cursor()
curson.execute('create table user(id varchar(20) primary key ,username varchar (50) )')
curson.execute('insert into user (id,username) values (%s,%s)',['1','lch'])
conn.commit()
curson.close()