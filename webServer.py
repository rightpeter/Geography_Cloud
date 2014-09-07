#!/usr/bin/env python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from tornado.options import define, options
from uploadHandler import UploadHandler
from getXYHandler import  GetXYHandler
from jsonGetXYHandler import JsonGetXYHandler
from getDetailHandler import GetDetailHandler
from jsonGetDetailHandler import JsonGetDetailHandler
from getPictureHandler import GetPictureHandler
from getOverviewHandler import GetOverviewHandler
from urlMapHandler import UrlMapHandler

define("port", default=3358, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler),
            (r'/urlmap', UrlMapHandler),
            (r'/new_building', UploadHandler),
            (r'/getxy', GetXYHandler),
            (r'/jsongetxy', JsonGetXYHandler),
            (r'/getpic', GetPictureHandler),
            (r'/getdetail/(\d+)$', GetDetailHandler),
            (r'/jsongetdetail$', JsonGetDetailHandler),
            (r'/getoverview/(\d+)$', GetOverviewHandler),
            (r'/indoor', IndoorHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class IndoorHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("mapdemo.html")

def main():
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
