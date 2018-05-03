#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/3 13:34
# @Author  : LCH
# @Site    : 
# @File    : TCP.py
# @Software: PyCharm
import socket,threading,time

#server code
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('listening...')

def tcplink(sock,addr):
    print('Accept new conn from %s:%s'%addr)
    sock.send(b'Welcome!') #socket send必须为bytes类型
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Conn from %s:%s closed..'%addr)

while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()


