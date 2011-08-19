

import eventlet

def closed_callback():
  print "called back"

def forward(source, dest, cb = lambda: None):
  while True:
    d = source.recv(32384)
    print(d)
    if d == '':
      cb()
      break
    dest.sendall(d)

listener = eventlet.listen(('10.210.65.126',8080))
while True:
  client , addr = listener.accept()
  server = eventlet.connect(('www.google.com',80))
  eventlet.spawn_n(forward, client, server, closed_callback)
  eventlet.spawn_n(forward, server, client)

  


	
