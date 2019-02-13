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
while 1:
    msg = input("输入你需要发送的信息:")
    msg = msg.encode(encoding='utf-8')
    s.send(msg)
    print(s.recv(1024).decode('utf-8'))
