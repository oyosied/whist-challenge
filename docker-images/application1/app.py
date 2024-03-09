import os

from flask import Flask, render_template
import psycopg2

app = Flask(__name__)
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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app_port)
