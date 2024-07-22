from flask import Flask

app = Flask(__name__)

@app.route('/')
def zipcode_data():
    return 'Hello, ZipCode!'