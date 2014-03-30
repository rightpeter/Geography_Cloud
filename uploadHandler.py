#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle

from db import *

#资料上传
class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('new_building.html')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        GCDatabase.reconnect()
        
        name = self.get_argument('name')
        try:
            lng = self.get_argument('lng')
        except:
            lng = 121.818034 
        try:
            lat = self.get_argument('lat')
        except:
            lat = 39.086543 
        storey = self.get_argument('storey')
        description = self.get_argument('description')

        if (self.get_argument('father')):
            fid = int(self.get_argument('father'))
            floor = int(self.get_argument('floor'))
        else:
            fid = 0
            floor = 0

        #存入info
        #GCDatabase.execute(u"""INSERT buildings(name, lng, lat, storey,
        #        description) VALUES(%s, %s, %s, %s, %s)""", name, lng, lat,
        #        storey, description) 

        GCDatabase.execute(u"""INSERT buildings(name, storey,
                description) VALUES(%s, %s, %s)""", name, storey, description) 

        cid = int(GCDatabase.query("""SELECT LAST_INSERT_ID() AS id;""")[0]['id'])

        GCDatabase.execute("""INSERT relation(fid, cid, storey) VALUES(%s, %s,
                %s)""", fid, cid, floor)

        home_path = './static/buildings/%s/' % cid

        #建立新文件夹
        if not os.path.isdir(home_path):
            os.makedirs(home_path)

        #存入图片
        if self.request.files:
            for i in range(0, len(self.request.files['myfile'])): 
                    myfile = self.request.files['myfile'][i] 
                    print myfile
                    path_image = home_path + '%d.jpg' % i
                    image = open(path_image, "w")
                    print "success to open" + path_image
                    image.write(myfile["body"])
                    image.close()
