#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 17:56
# @Author  : LCH
# @Site    : 
# @File    : 用gui控制键盘鼠标.py
# @Software: PyCharm
import pyautogui
import selenium
from __future__ import absolute_import
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

if __name__ == '__main__':
    orgin_url = ['https://pan.baidu.com/']
    driver = webdriver.Firefox()
    driver.get(orgin_url[0])
    time.sleep(5)
    elem_static = driver.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
    elem_static.click()
    time.sleep(0.5)
    elem_username = driver.find_element_by_id("TANGRAM__PSP_4__userName")
    elem_username.clear()
    elem_username.send_keys(u"XXXXXXXXXX")  # 填入帐号
    elem_userpas = driver.find_element_by_id("TANGRAM__PSP_4__password")
    elem_userpas.clear()
    elem_userpas.send_keys(u"XXXXXXXXX")  # 密码
    elem_submit = driver.find_element_by_id("TANGRAM__PSP_4__submit")
    elem_submit.click()
    time.sleep(10)
    driver.close()

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


positon=pyautogui.locateOnScreen('2.png')
print(positon)
x,y=pyautogui.center((positon))
print(x,y)
num=6
while num>1:
    num=num-1
    pyautogui.click(x,y,pause=0.5)
    time.sleep(1)
