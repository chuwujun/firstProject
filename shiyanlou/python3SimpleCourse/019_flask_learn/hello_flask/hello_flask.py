#!/usr/bin/env python3

import flask

#create the applocation
App=flask.Flask(__name__)

@App.route('/')
def index():
    return flask.render_template('index.html')

@App.route('/hello/<name>/')
def hello(name):
    """Display the page greats who ever comes to visit it."""
    return flask.render_template('hello.html',name=name)

if __name__ == '__main__':
    App.debug=True
    App.run()
