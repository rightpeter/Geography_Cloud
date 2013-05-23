#!/usr/bin/env python

import logging
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import uuid

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/detail/(\d+)$", DetailHandler),
            (r"/detail/(\d+)/introduce$", IntroduceHandler),
            (r"/detail/(\d+)/gallery$", GalleryHandler), 
        ]
        settings = dict(
            cookie_secret = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class DetailHandler(tornado.web.RequestHandler):
    def get(self, Userid):
        path = '/static/building' + Userid
        pic_path = path + '/image/1.jpg'
        intro_path = path + '/introduce.txt'
        self.render("detail.html", id=Userid, introcuction=intro_path,
                picture=pic_path)

class IntroduceHandler(tornado.web.RequestHandler):
    def get(self, Userid):
        self.render("introduce.html", id=Userid)

class GalleryHandler(tornado.web.RequestHandler):
    def get(self, Userid):
        self.render("gallery.html", id=Userid)


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main() 
