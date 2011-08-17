

import tornado.ioloop
import tornado.web

from tornado.httpclient import HTTPClient

class Http_client(tornado.web.RequestHandler):
  def get(self):
    http_client = HTTPClient()
    try:
      response = http_client.fetch("http://www.google.com")
    except httpclient.HTTPError, e:
      print(e)
    self.write(response)
