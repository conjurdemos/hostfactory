#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os

response_message = bytes('''
<html>
  <head>
    <title>Conjur Hostfactory Example</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>My database username is: {}</p>
    <p>My database password is: {}</p>
  </body>
</html>
'''.format(os.getenv('DB_USER', 'ERROR'),
           os.getenv('DB_PASS', 'ERROR')))

class ServerHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.protocol_version='HTTP/1.1'
    self.send_response(200, 'OK')
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(response_message)

if __name__ == "__main__":
  server_port = int(os.getenv('PORT', 80))
  server_address = ('', server_port)
  httpd = HTTPServer(server_address, ServerHandler)
  print 'Serving on port ' + str(server_port) + '...'
  httpd.serve_forever()