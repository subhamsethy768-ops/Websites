from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8000  # You can change this port

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.path = 'index.html'
        return super().do_GET()

if __name__ == "__main__":

    server_address = ('', PORT)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()
