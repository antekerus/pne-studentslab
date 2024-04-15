import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080
bases = ["A", "C", "G", "T"]

socketserver.TCPServer.allow_reuse_address = True


class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/" or self.path == "/index.html":
            contents = Path("index.html").read_text()
            self.send_response(200)
        else:
            try:
                contents = Path(f"html/info/{bases}, + .html").read_text()
                self.send_response(200)
            except FileNotFoundError:
                contents = Path("html/error.html").read_text()
                self.send_response(400)

        contents_bytes = contents.encode()
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)

        return


with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()