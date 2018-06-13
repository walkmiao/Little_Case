#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : web-1.py
# @Author: lch
# @Date  : 2018/5/21
# @Desc  :
import web

urls = (
    # '/(.*)', 'hello',
    '/hello_1[/]?.*', 'hello_1',
    '/hello_2/(.*)', 'hello_2',
)
app=web.application(urls,globals())
render=web.template.render('templates/')

class hello_1():

    def GET(self):
        i = web.input(name=None)
        return render.hello1(i.name)
class hello_2():
    def GET(self,name):
        return render.hello2(name)

if __name__=='__main__':
    app.run()