from flask import Flask, render_template
import psycopg2
from psycopg2.extras import DictCursor

app = Flask(__name__)

# koneksi ke database Postgres
def get_db_connection():
    conn = psycopg2.connect(
        host="your_host",
        database="your_db",
        user="your_user",
        password="your_password"
    )

    return conn

def get_question():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM master_kata ")

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)

    cursor.execute("SELECT * FROM master_kata")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', data=rows)

if __name__ == '__main__':
    app.run(debug=True)