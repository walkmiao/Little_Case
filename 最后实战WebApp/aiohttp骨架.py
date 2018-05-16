#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : aiohttp骨架.py
# @Author: lch
# @Date  : 2018/5/14
# @Desc  :
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9600)
    logging.info('server started at http://127.0.0.1:9600...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()