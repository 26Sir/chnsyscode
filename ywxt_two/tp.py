#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, base64
from flask import Flask, request

app = Flask(__name__)


@app.route('/api/base642img', methods=['POST'])
def base642img():
    strs = request.form['pngbase64']
    imgdata = base64.b64decode(strs)
    file = open('test.jpg', 'wb')
    file.write(imgdata)
    file.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005', debug=True)