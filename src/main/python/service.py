import time
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from resistor import *
from urllib.parse import urlparse
from urllib.parse import parse_qs
import re

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

PAGE_404_MESSAGE = '''
                   <html><head><title>404 - Page Not Found</title></head>
                   <body><p>Sorry, that page does not exist.</p></body>
                   </html>
                   '''
PAGE_400_MESSAGE = '''
                   <html><head><title>400 - Query String Error</title></head>
                   <body><p>There was an error with the query string,
                   please check it and try again.</p></body>
                   </html>
                   '''


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    print(time.asctime(), 'Server started - {}:{}'.format(
        HOST_NAME, PORT_NUMBER))
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


class HTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path).path
        if not parsed_path.startswith('/decode'):
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(PAGE_404_MESSAGE, 'UTF-8'))
        elif not self._validateUrl(self.path):
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(PAGE_400_MESSAGE, 'UTF-8'))
        else:
            self._respond()

    def _handle_http(self, path):
        parsed_url = urlparse(path)

        query = parse_qs(parsed_url.query)

        if len(query.keys()) != len(query.values()):
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return bytes(PAGE_400_MESSAGE, 'UTF-8')

        colors = [value[0] for key, value
                  in parse_qs(parsed_url.query).items()]
        try:
            result = decodeResistance(colors)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        except (ValueError):
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return bytes(PAGE_400_MESSAGE, 'UTF-8')

        content = '''
        <html><head><title>Resistor Band Checker</title></head>
        <body><p>{}</p></body>
        </html>
        '''.format(result)
        return bytes(content, 'UTF-8')

    def _respond(self):
        response = self._handle_http(self.path)
        self.wfile.write(response)

    def _validateUrl(self, path):
        fourBandPattern = re.compile(r'''
            ^\/decode\?(band\d=\w+\&){3}band\d=\w+$''', re.VERBOSE)
        fiveBandPattern = re.compile(r'''
            ^\/decode\?(band\d=\w+\&){4}band\d=\w+$''', re.VERBOSE)

        if fourBandPattern.search(path) or fiveBandPattern.search(path):
            return True

        return False


run(handler_class=HTTPHandler)
