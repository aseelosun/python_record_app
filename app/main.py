from flask import Flask
import psycopg2
import os
import random
import time

app = Flask(__name__)

def get_connection():
    while True:
        try:
            return psycopg2.connect(
                host=os.environ['DB_HOST'],
                dbname=os.environ['DB_NAME'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD']

            )
        except Exception as e:
            time.sleep(1)

@app.route('/addrecord')
def add_record():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS records(
                        id SERIAL PRIMARY KEY,
                    value TEXT
                    )
                    """)
        cur.execute("INSERT INTO records (value) VALUES (%s)", (str(random.randint(1, 1000)),))
        conn.commit()
        conn.close()
        return "record added"
    except Exception as e:
        return f'error: {str(e)}', 500

@app.route('/deleterecord')
def delete_record():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM records WHERE id = (SELECT id FROM records ORDER BY id ASC LIMIT 1)" )
    conn.commit()
    conn.close()
    return "record deleted"

@app.route('/testdb')
def test_db():
    try:
        conn = psycopg2.connect(
            host="db",  
            database="records_db",
            user="user",
            password="secret"
        )
        conn.close()
        return "PostgreSQL connection successful"
    except Exception as e:
        return f"PostgreSQL connection failed: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
