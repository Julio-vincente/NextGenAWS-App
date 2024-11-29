from flask import Flask, render_template, g
import pymysql

app = Flask(__name__)

# Configurações do RDS
RDS_CONFIG = {
    'host': 'seu-endereco-rds.amazonaws.com',  # Endereço do seu RDS
    'user': 'seu-usuario',                     # Nome de usuário
    'password': 'sua-senha',                   # Senha
    'database': 'seu-banco',                   # Nome do banco de dados
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
    """Exibe a lista de livros."""
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
    app.run(host="0.0.0.0", port=5000)