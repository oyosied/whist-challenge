from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="db",
    user="postgres",
    password="Aa@123456"
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
