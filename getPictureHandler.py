#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from myTools import *

class GetPictureHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('matchpicture.html')

    def post(self):
        lng = float(self.get_argument('lng'))
        lat = float(self.get_argument('lat'))
        dis = 1

        #存入图片
        if self.request.files:
            pic = self.request.files['myfile'][0]

        buildings_list = getNearby((lat, lng), dis)
        print buildings_list
        self.write('%s' % matchBuildings(pic, buildings_list))
