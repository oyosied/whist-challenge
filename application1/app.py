import os
import socket
from datetime import datetime

from flask import Flask, render_template, request, jsonify
import psycopg2
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

app_port = os.getenv('FLASK_APP_PORT', 5001)
db_password = os.getenv('POSTGRES_PASSWORD')
db_username = os.getenv('POSTGRES_USERNAME')
db_name = os.getenv('DB_NAME')

conn = psycopg2.connect(
    host="db",
    database=db_name,
    user=db_username,
    password=db_password
)

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

def increment_global():
    db_cursor = conn.cursor()
    try:
        sql_query = "UPDATE global_counter SET hit_counter = hit_counter + 1"
        db_cursor.execute(sql_query)
        conn.commit()
    except:
        conn.rollback()

@app.route('/')
def index():
    print(IPAddr)
    increment_global()
    client_ip = request.headers.getlist('X-Forwarded-For')[0]
    replica_ip = request.cookies.get('replica_ip', '')
    replica_ip = replica_ip.split(':')[0]

    now = datetime.now()

    db_cursor = conn.cursor()
    try:
        db_cursor.execute(
            "INSERT INTO access_log (client_ip, date_time, replica_ip) VALUES (%s, %s, %s)",
            (client_ip, now, replica_ip)
        )
        conn.commit()
    except:
        conn.rollback()

    return jsonify(replica_ip=replica_ip)

@app.route('/showcount')
def show_count():
    db_cursor = conn.cursor()
    db_cursor.execute("SELECT * FROM global_counter")
    row = db_cursor.fetchone()
    return jsonify(row[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app_port)
