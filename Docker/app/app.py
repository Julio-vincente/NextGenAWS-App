from flask import Flask, render_template, g
import pymysql

app = Flask(__name__)

RDS_CONFIG = {
    'host': 'aaaa',
    'user': 'aaaa',
    'password': 'aaaa',
    'database': 'aaaa',
}

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = pymysql.connect(**RDS_CONFIG)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/books')
def books():
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()
    return render_template('books.html', books=books)

@app.route('/authors')
def authors():
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
    return render_template('authors.html', authors=authors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)