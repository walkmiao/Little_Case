#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 14:02
# @Author  : LCH
# @Site    : 
# @File    : Client.py
# @Software: PyCharm

#client code
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))  #接受server发来的消息时注意解码，因为send默认发的是bytes类型
for data in [b'ALISA',b'BOB',b'FOCUS']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()