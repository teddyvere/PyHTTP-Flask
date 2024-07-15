Flask is a web framework that makes it easy to build web applications in Python. But you can do the same things without Flask, and this example shows you the rough idea. The example is a simple web server that serves two HTML pages: an index page and a form page. The index page displays a welcome message, and the form page displays a form with name and email fields. When the form is submitted, the server reads the form data and returns a response with the submitted values.

And without Flask, you'd have to write something like this.
The amount of code in the two examples is roughly the same, but the Flask code is more readable and easier to understand. And as apps get bigger and more complex, the Flask code will be easier to maintain and extend.

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'r') as file:
                self.wfile.write(file.read().encode())
        elif self.path == '/form':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('form.html', 'r') as file:
                self.wfile.write(file.read().encode())

        def do_POST(self):
        if self.path == '/form':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            parsed_data = urlparse.parse_qs(post_data.decode())

            name = parsed_data.get('name')[0]
            email = parsed_data.get('email')[0]

            response = f'Name: {name}, Email: {email}'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

run()
```
