#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 9:03
# @Author  : lch
# @File    : requests_module.py
import requests
# 传递url参数
payload = {'key1': 'value1', 'key2': 'value2'}  # 参数字典配置
html = requests.get(url='http://httpbin.org', params=payload)
print(html.url)
