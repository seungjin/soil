
import sys
import os
import logging

import tornado.httpserver
import tornado.ioloop
import tornado.web

from django.conf import settings

#soil libraries
from cloudservice.hello import *
from cloudservice.http_client import Http_client


from ConfigParser import RawConfigParser
config = RawConfigParser()
config.read('/Users/seungjin/Documents/soil_home/creadentials.ini')

application = tornado.web.Application([
  (r"/cloudservice/hello", HelloHandler),
  (r"/cloudservice/http_client_test", Http_client),
])


# start the server
if __name__ == "__main__":
  http_server = tornado.httpserver.HTTPServer(application,
                                              ssl_options={
                                                "certfile": config.get('domain_cert_and_key','DOMAIN_CERT'),
                                                "keyfile": config.get('domain_cert_and_key','DOMAIN_KEY')
                                                }
                                              )
  http_server.listen(8080)
  tornado.ioloop.IOLoop.instance().start()



