#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 15:14
# @Author  : LCH
# @Site    : 
# @File    : hello.py
# @Software: PyCharm

# def application(environ,start_response):
#     start_response('200 ok',[('Content-Type','text/html')])
#     body='<h1>hello,%s</h1>'%(environ['PATH_INFO'][1:] or 'web')
#     return [body.encode('utf-8')]

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ)
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'] or 'web')
    return [body.encode('utf-8')]