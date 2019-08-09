#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Healthcheck for use with gcp
"""

from flask import Flask, jsonify
import os
import socket
from contextlib import closing


app = Flask(__name__)
port = int(os.environ.get('PORT', 9000))
checkhost = os.environ.get('CHECKHOST', '127.0.0.1')
checkport = int(os.environ.get('CHECKPORT', 80))
debug = bool(os.environ.get('DEBUG', True))


def check_port(host='127.0.0.1', port=80):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return (sock.connect_ex((host, port)) == 0)


@app.route('/')
def index():
    opened = check_port(checkhost, checkport)
    response = jsonify(opened)
    response.status_code = 200 if opened else 503
    return response


def run():
    """

    """
    app.run(host='0.0.0.0', port=port, debug=debug)


if __name__ == '__main__':
    run()
