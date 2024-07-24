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

if __name__ == '__main__':
    app.run(port=8000)