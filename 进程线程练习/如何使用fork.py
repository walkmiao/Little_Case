#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 如何使用fork.py
# @Author: lch
# @Date  : 2018/10/12
# @Desc  :
import socket, os

"""
   简单网络程序，每次连接后派生的子进程终止后都会成为僵死进程
"""

serSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serSock.bind(('127.0.0.1', 8888))
serSock.listen(5)

while True:
    conn, addr = serSock.accept()
    print(addr)
    pid = os.fork()
    if pid:
        """
           父进程关闭子进程的已连接套接字
        """
        conn.close()
        continue
    elif pid == 0:
        """
           子进程关闭父进程的监听套接字
        """
        serSock.close()
        data = conn.recv(1024).decode('utf-8')
        conn.sendall(("echo: " + data).encode('utf-8'))
        conn.close()
        os._exit(0)
