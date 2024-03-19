import os
import socket
from datetime import datetime

from flask import Flask, render_template, request, jsonify
import psycopg2
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

@app.route('/')
def index():
    return jsonify(replica_ip="yossi yos")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
