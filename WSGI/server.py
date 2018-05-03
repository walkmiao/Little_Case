#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 15:14
# @Author  : LCH
# @Site    : 
# @File    : server.py
# @Software: PyCharm
from wsgiref.simple_server import make_server
from WSGI.hello import application
httpd=make_server('localhost',9000,application)
print('Serving HTTP on port 8000.. ')
httpd.serve_forever()