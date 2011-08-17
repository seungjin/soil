



import tornado.ioloop
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
  def get(self):
    self.write("world!")
