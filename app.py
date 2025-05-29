from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'cafe'

DB_CONFIG = {
    'host': 'localhost',
    'database': 'meu_site_db',
    'user': 'root',
    'password': ''
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor(buffered=True)
                sql = "SELECT id, email, senha FROM cadastro WHERE email = %s"
                cursor.execute(sql, (email,))
                user = cursor.fetchone()

                if user and check_password_hash(user[2], password):
                    session['loggedin'] = True
                    session['id'] = user[0]
                    session['email'] = user[1]
                    flash('Login bem-sucedido!', 'success')
                    return redirect(url_for('site'))
                else:
                    flash('E-mail ou senha incorretos.', 'error')
            except Error as err:
                flash(f'Erro no login: {err}', 'error')
            finally:
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()
                if conn is not None and conn.is_connected():
                    conn.close()
        else:
            flash('Erro: Não foi possível conectar ao banco de dados para login.', 'error')
    return redirect(url_for('index'))

@app.route('/site')
def site():
    if 'loggedin' in session and session['loggedin']:
        return render_template('site.html')
    else:
        flash('Você precisa estar logado para acessar esta página.', 'error')
        return redirect(url_for('index'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_form():
    if request.method == 'POST':
        email = request.form['email']
        telefone = request.form.get('phone', '')
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        if not email or not password or not confirm_password:
            flash('Erro: Por favor, preencha todos os campos obrigatórios (E-mail e Senha).', 'error')
        elif password != confirm_password:
            flash('Erro: As senhas não coincidem. Por favor, digite novamente.', 'error')
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

            conn = get_db_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    sql = "INSERT INTO cadastro (email, telefone, senha) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (email, telefone, hashed_password))
                    conn.commit()
                    flash('Cadastro realizado com sucesso!', 'success')
                    return redirect(url_for('cadastro_form'))
                except Error as err:
                    if err.errno == 1062:
                        flash('Erro: Este e-mail já está cadastrado. Por favor, use outro.', 'error')
                    else:
                        flash(f'Erro ao cadastrar: {err}', 'error')
                    conn.rollback()
                finally:
                    if 'cursor' in locals() and cursor is not None:
                        cursor.close()
                    if conn is not None and conn.is_connected():
                        conn.close()
            else:
                flash('Erro: Não foi possível conectar ao banco de dados.', 'error')

    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)