#! /bin/bash
# coding=utf8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<a href="info"> <h1>Hello World!</h1></a>'


@app.route('/info')
def get_someinfo():
    return u"<b>版权所有 违反必究"

if __name__ == '__main__':
    app.run()
