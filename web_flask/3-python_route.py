#!/usr/bin/python3
'''Flask web application.
'''
from flask import Flask


app = Flask(__name__)
'''Flask application instance.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''Home Page.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnb page.'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''C page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''Python page.'''
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
