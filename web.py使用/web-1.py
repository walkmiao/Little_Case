#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : web-1.py
# @Author: lch
# @Date  : 2018/5/21
# @Desc  :
import web

urls = (
    # '/(.*)', 'hello',
    '/hello1', 'hello_1',
    '/hello2/(.*)', 'hello_2',
)
app=web.application(urls, globals())
render=web.template.render('templates/')

class hello():
    def GET(self, name):
        if not name:
            name = 'world'
        return 'hello ' + name +' !'

class hello_1():

    def GET(self):
        i = web.input()
        print(i)
        count=i.count
        return render.hello1(count)


class hello_2():
    def GET(self, name):
        return render.hello2(name)


if __name__=='__main__':
    app.run()