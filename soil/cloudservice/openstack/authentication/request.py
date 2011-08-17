

# authentification request

# testing

#US-based account authenticate : https://auth.api.rackspacecloud.com/v1.0

# for testing, use config file, will be from database
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('')

user = config.get('Section1', 'user')
key = config.get('Section1', 'key')


import httplib
import urllib
from urlparse import urlparse

endpoint = "https://auth.api.rackspacecloud.com"
o = urlparse(endpoint)
path = "/v1.0"
method = "GET"
param = None
headers = {
  "X-Auth-User": user,
  "X-Auth-Key" : key
}
  
