import sqlite3
from flask import Flask, request, jsonify, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('usuarios.db')
    conn.row_factory = sqlite3.Row  # Para que os resultados sejam retornados como dicionários
    return conn

# Rota de Cadastro
@app.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()

    # Validar dados recebidos
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    if not nome or not email or not senha:
        return jsonify({"error": "Todos os campos são obrigatórios!"}), 400

    # Conectar ao banco de dados e verificar se o e-mail já existe
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    usuario = cursor.fetchone()

    if usuario:
        return jsonify({"error": "E-mail já cadastrado!"}), 400

    # Criar novo usuário
    hashed_senha = generate_password_hash(senha, method='sha256')
    cursor.execute('INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)', (nome, email, hashed_senha))
    conn.commit()
    conn.close()

    return jsonify({"message": "Cadastro realizado com sucesso!"}), 201

# Rota de Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validar dados recebidos
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({"error": "E-mail e senha são obrigatórios!"}), 400

    # Conectar ao banco de dados e buscar o usuário
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    usuario = cursor.fetchone()
    conn.close()

    if not usuario or not check_password_hash(usuario['senha'], senha):
        return jsonify({"error": "Credenciais inválidas!"}), 401

    return jsonify({"message": "Login bem-sucedido!", "redirect": "/home"}), 200

if __name__ == '__main__':
    app.run(debug=True)
