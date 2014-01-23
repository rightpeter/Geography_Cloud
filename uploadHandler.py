#!/usr/bin/python
#encoding: utf-8

import tornado.web
import tornado.ioloop
import os.path
import pickle

#资料上传
class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('new_building.html')

    def post(self):
        self.set_header("Content-Type", "text/plain")

        #设置父亲
        home_path = './static/buildings/' + self.get_argument("id") + '/'
        if (self.get_argument("father")):
            print "has father"
            father_path = './static/buildings/' + self.get_argument("father") + '/info.pickle'
            with open(father_path, 'rb') as tmp:
                father_info = pickle.load(tmp)
            father_info['children'].append(self.get_argument("id"))
            with open(father_path, 'wb') as tmp:
                pickle.dump(father_info, tmp)
                
        #建立新文件夹
        if not os.path.isdir(home_path):
            os.makedirs(home_path)

        #存入info
        path_info = home_path + 'info.pickle'
        info = open(path_info, "wb")
        print "succes to open " + path_info
        info_dict = {"id":self.get_argument("id"),
                     "father":self.get_argument("father"),
                     "position":(float(self.get_argument("X")), float(self.get_argument("Y"))),
                     "children":[]}
        pickle.dump(info_dict, info) 

        #存入图片
        if self.request.files:
            for i in range(0, len(self.request.files['myfile'])): 
                    myfile = self.request.files['myfile'][i] 
                    path_image = home_path + '%d.jpg' % i
                    fin = open(path_image, "w")
                    print "success to open" + path_image
                    fin.write(myfile["body"])
                    fin.close()

