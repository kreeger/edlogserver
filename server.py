"""WIP: Describe all available HTTP routes to access internal data."""

from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    """Responsible for serving responses to HTTP requests."""

    def do_GET(self):
        """Insert docstring here."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

    @classmethod
    def start(cls, config):
        """Insert docstring here."""
        print('Starting server...')

        # Server settings
        # Choose port 8080, for port 80, which is normally used for a http
        # server, you need root access
        httpd = HTTPServer(('127.0.0.1', config.port), cls)
        print('Running server on port %s.' % config.port)
        httpd.serve_forever()
