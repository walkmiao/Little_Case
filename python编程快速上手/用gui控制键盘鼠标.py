#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 17:56
# @Author  : LCH
# @Site    : 
# @File    : 用gui控制键盘鼠标.py
# @Software: PyCharm
import pyautogui
import time
# print('Press Ctrl-C to quit')
#
# try:
#     x,y=pyautogui.position()
#     positionStr='X: '+str(x)+'Y: '+str(y)
#     time.sleep(5)
#     print(positionStr+' check')
#     pyautogui.click()
#     distance=200
#     while distance>0:
#         pyautogui.dragRel(distance,0,duration=0.2)
#         distance=distance-5
#         pyautogui.dragRel(0,distance,duration=0.2)
#         pyautogui.dragRel(-distance,0,duration=0.2)
#         distance=distance-5
#         pyautogui.dragRel(0,-distance,duration=0.2)
# except KeyboardInterrupt:
#     print('end' + positionStr)

positon=pyautogui.locateOnScreen('1.png')
print(positon)
x,y=pyautogui.center((positon))
print(x,y)
num=6
while num>1:
    num=num-1
    pyautogui.click(x,y,pause=0.5)
    # time.sleep(1)
