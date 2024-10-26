import sqlite3
from models.livro import Book
from models.usuario import User_Student


BOOKS_DB_PATH = 'data/books.db'
USERS_DB_PATH = 'data/users.db'

def conectar_books():
    conn = sqlite3.connect(BOOKS_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def conectar_users():
    conn = sqlite3.connect(USERS_DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn_books = conectar_books()
    cursor_books = conn_books.cursor()

    # Não coloquei todos os atributos do objeto na tabela por questão de privacidade, (atributos user e data_emprestimo)
    cursor_books.execute('''CREATE TABLE IF NOT EXISTS livros (id_livro INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, ano INTEGER, disponivel BOOLEAN DEFAULT FALSE)''')
    conn_books.commit()
    conn_books.close()

    conn_users = conectar_users()
    cursor_users = conn_users.cursor()

    cursor_users.execute('''CREATE TABLE IF NOT EXISTS usuarios (id_usuario INTEGER PRIMARY KEY,nome TEXT)''')
    conn_users.commit()
    conn_users.close()


def adicionar_livro(livro):
    conn = conectar_books()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (id_livro, titulo, autor, ano, disponivel) VALUES (?, ?, ?, ?, ?)",(livro.id_livro, livro.titulo, livro.autor, livro.ano, livro.disponivel))
    conn.commit()
    conn.close()


def adicionar_usuario(usuario):
    conn = conectar_users()
    cursor = conn.cursor()  
    cursor.execute("INSERT INTO usuarios (id_usuario, nome) VALUES (?, ?)",(usuario.id_usuario, usuario.nome))
    conn.commit()
    conn.close()

def deletar_livro(id_livro):
    conn = conectar_books()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM livros WHERE id_livro = ?", (id_livro,))
    conn.commit()
    conn.close()

def deletar_usuario(id_usuario):
    conn = conectar_users()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id_usuario = ?", (id_usuario,))
    conn.commit()
    conn.close()

def atualizar_livro(livro):
    conn = conectar_books()
    cursor = conn.cursor()
    cursor.execute("UPDATE livros SET disponivel = ? WHERE id_livro = ?", (livro.disponivel, livro.id_livro))
    conn.commit()
    conn.close()