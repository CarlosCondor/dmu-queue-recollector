#!/usr/bin/python
import json
import time
import BaseHTTPServer
from pprint import pprint
import urlparse
HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 9000 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_HEAD(s):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
        def do_GET(s):
                """Respond to a GET request."""
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
                s.wfile.write("<html><head><title>Title goes here.</title></head>")
                s.wfile.write("<body><form action='.' method='POST'><input name='x' value='1' /><input type='submit' /></form><p>This is a test.</p>")
                # If someone went to "http://something.somewhere.net/foo/bar/",
                # then s.path equals "/foo/bar/".
                s.wfile.write("<p>GET: You accessed path: %s</p>" % s.path)
                s.wfile.write("</body></html>")
                pprint (vars(s))
        def do_POST(s):
                """Respond to a POST request."""
                # Extract and print the contents of the POST
                length = int(s.headers['Content-Length'])
                post_data = urlparse.parse_qs(s.rfile.read(length).decode('utf-8'))
                import ipdb;ipdb.set_trace()    
                
                print "==="
                array_data = post_data
                print type(array_data)
                print array_data
                #json_data = json.loads(array_data[0])
                #print json_data, type(json_data)
                #print json_data[0]['key']
                print "==="
                for key, value in post_data.iteritems():
                    print "%s=%s" % (key, value)

                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.end_headers()
        # def do_POST(s):

        #         """Respond to a POST request."""
        #         s.send_response(200)
        #         s.send_header("Content-type", "text/html")
        #         s.end_headers()
        #         s.wfile.write("<html><head><title>Title goes here.</title></head>")
        #         s.wfile.write("<body><p>This is a test.</p>")
        #         s.wfile.write("<body><form action='.' method='POST'><input type='text' name='xxxxxxxxxxxx' value='0000000000000000000000' /><input type='submit' /></form><p>This is a test.</p>")
        #         # If someone went to "http://something.somewhere.net/foo/bar/",
        #         # then s.path equals "/foo/bar/".
        #         s.wfile.write("<p>POST: You accessed path: %s</p>" % s.path)
        #         s.wfile.write("</body></html>")
        #         pprint (vars(s))
        #         pprint (vars(s.connection))
        #         pprint (vars(s.headers))
        #         pprint (vars(s.request))
        #         pprint (vars(s.rfile))
        #         pprint (vars(s.server))
        #         pprint (vars(s.wfile))
        #         pprint (vars(s.fp))
        #         """pprint (vars(s.request))"""

if __name__ == '__main__':
        server_class = BaseHTTPServer.HTTPServer
        httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
        print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
        try:
                httpd.serve_forever()
        except KeyboardInterrupt:
                pass
        httpd.server_close()
        print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)