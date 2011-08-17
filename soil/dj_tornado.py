
import sys
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web

from django.conf import settings

#soil libraries
from cloudservice.hello import *


application = tornado.web.Application([
  (r"/cloudservice/hello", HelloHandler),
])


# start the server
if __name__ == "__main__":
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(80)
  tornado.ioloop.IOLoop.instance().start()
