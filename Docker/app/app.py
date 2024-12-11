from flask import Flask, render_template, g, jsonify
import pymysql
import os
import logging

app = Flask(__name__)

# Configuração do banco de dados
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

RDS_CONFIG = {
    "host": db_host,
    "user": db_user,
    "password": db_password,
    "database": db_name
}

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para obter conexão com o banco
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        try:
            db = g._database = pymysql.connect(**RDS_CONFIG)
            logger.info("Conexão ao banco de dados estabelecida.")
        except pymysql.MySQLError as e:
            logger.error(f"Erro ao conectar ao banco de dados: {e}")
            raise
    return db

# Fechamento da conexão ao encerrar o contexto da aplicação
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        logger.info("Conexão ao banco de dados encerrada.")

# Rotas
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/books')
def books():
    try:
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute('SELECT * FROM books')
            books = cursor.fetchall()
        return render_template('books.html', books=books)
    except Exception as e:
        logger.error(f"Erro ao buscar livros: {e}")
        return jsonify({"error": "Erro ao buscar livros"}), 500

@app.route('/authors')
def authors():
    try:
        db = get_db()
        with db.cursor() as cursor:
            cursor.execute('SELECT * FROM authors')
            authors = cursor.fetchall()
        return render_template('authors.html', authors=authors)
    except Exception as e:
        logger.error(f"Erro ao buscar autores: {e}")
        return jsonify({"error": "Erro ao buscar autores"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 80))
    app.run(host="0.0.0.0", port=port)
