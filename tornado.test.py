# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("tet,中午commmmmmm")


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/test", TestHandler),
    ])        

if __name__=="__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()