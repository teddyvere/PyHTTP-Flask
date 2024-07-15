# PyHTTP-Flask

Create a sinple HTTP server using only Python3.

## Simple HTTP Serverr

Create a simple HTTP server using Python.

```
python3 -m http.server
```
Now show a static file to the user from this directory.

Add a simple page.html file to the directory.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page</title>
</head>
<body>
    <h1>Welcome to the Page</h1>
    <p>This is a simple page.</p>
    <a href="https://www.zipcodewilmington.com">Go to ZipCode's website</a>
</body>
</html>
```

Now add a page to the server that displays a message to the user. Make this a file named `page.py`.

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, World!')


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
```

`Do a GIT triple: Add, Commit, Push` to capture your work.

## Description
Create a simple HTTP server using Python and Flask.

Check out the Flask documentation at https://flask.palletsprojects.com/en/2.0.x/

And think of an answer to the following questions:

#### What is Flask?
#### What is a web framework?

And why do you need one?

## Requirements

- in a terminal...make certain you have the following installed:
- Python 3.8+
- Flask
- create a virtual environment using `python3 -m venv .venv`
- activate the virtual environment using `source .venv/bin/activate`
- install Flask using `pip install Flask`

THis is a simple HTTP server using Python. It uses the Flask library to create a simple server that listens on port 5000.

## Usage


Create the contents of the file `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def zipcode_data():
    return 'Hello, ZipCode!'
```

This will start the web server and you can access it by going to `http://127.0.0.1:5000` in your browser.

`Do a GIT triple: Add, Commit, Push` to capture your work.

## Add two pages to Flask App

The first page should be a simple HTML page that displays a message to the user. The second page should be a simple form that accepts a user's name and email address. When the user submits the form, the data should be sent to the server and displayed on the form page.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Name: {name}, Email: {email}'
    # else: the request method is GET
    return render_template('form.html')
```

Flask is a web framework that makes it easy to build web applications in Python. It provides a simple way to define routes and handle requests. In the example above, we define two routes: one for the index page and one for a form page. The index route returns a simple HTML page, while the form route handles both GET and POST requests. When a POST request is made, it reads the form data and returns a response with the submitted values. When a GET request is made, it returns the form page.


`Do a GIT triple: Add, Commit, Push` to capture your work.

## HTML files

These are the two HTML files that the Flask app uses to display the index and form pages.

index.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Index</title>
</head>
<body>
    <h1>Welcome to the Index Page</h1>
</body>
</html>
```

form.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Form</title>

</head>
<body>
    <h1>Welcome to the Form Page</h1>
    <form action="/form" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

`Do a GIT triple: Add, Commit, Push` to capture your work.

Now add a link from the index page to the form page.

```html
<body>
    <h1>Welcome to the Index Page</h1>
    <a href="/form">Go to Form</a>
</body>
```

`Do a GIT triple: Add, Commit, Push` to capture your work.

#### Perhaps you are starting to see a pattern here??

## Without Flask, pure Python

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
