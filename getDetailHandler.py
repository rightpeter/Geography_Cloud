#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle
import json

from db import *
from myTools import *

#获取详细
class GetDetailHandler(tornado.web.RequestHandler):
    def get(self, bid):
        detail = GCDatabase.query("""SELECT * FROM buildings WHERE id=%s""", bid)
        detail = detail[0]
        print detail 

        sonlist = GCDatabase.query("""SELECT cid, storey FROM relation
                WHERE fid=%s""", bid)

        storey = int(detail['storey'])
        for i in range(1, storey+1):
            tmp = 'level%s' % i
            detail[tmp] = []
            for son in sonlist:
                if son['storey'] == i:
                    detail[tmp].append(int(son['cid']))

        print detail
        encodedjson = json.dumps(detail, cls=CJsonEncoder)
        self.write(encodedjson)
