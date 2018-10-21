import time
from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from resistor import *
from urllib.parse import urlparse
from urllib.parse import parse_qs

HOST_NAME = 'localhost'
PORT_NUMBER = 8000


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
            content = '''
            <html><head><title>404 - Page Not Found</title></head>
            <p>Sorry, that page does not exist</p>
            </body></html>
            '''
            self.wfile.write(bytes(content, 'UTF-8'))
        else:
            self._respond()

    def _handle_http(self, path):
        errorMessage = '''
        There was an error with the query string,
         please check it and try again.
        '''
        parsed_url = urlparse(path)
        colors = [value[0] for key, value
                  in parse_qs(parsed_url.query).items()]
        try:
            result = createFormattedResistanceString(colors)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        except (ValueError):
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return bytes(errorMessage, 'UTF-8')

        content = '''
        <html><head><title>Resistor Band Checker</title></head>
        <p>{}</p>
        </body></html>
        '''.format(result)
        return bytes(content, 'UTF-8')

    def _respond(self):
        response = self._handle_http(self.path)
        self.wfile.write(response)


run(handler_class=HTTPHandler)
