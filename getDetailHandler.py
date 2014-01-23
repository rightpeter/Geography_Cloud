#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

#获取详细
class GetDetailHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("detail.html")

    def post(self):
        self.set_header("Content-Type", "application/json")
        building_id = self.get_argument("id")
        building_path = './static/buildings/' + building_id + '/info.pickle'
        with open(building_path, 'rb') as tmp:
            building_dict = pickle.load(tmp)
        encodedjson = json.dumps(building_dict)
        self.write(encodedjson)

