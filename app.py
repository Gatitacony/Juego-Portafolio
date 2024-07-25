from flask import Flask, render_template, request, redirect, url_for, session
from db import get_db_connection, init_db, add_user
import os
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

config_type = os.getenv('FLASK_CONFIG_TYPE', 'development')
if config_type == 'development':
    app.config.from_object(DevelopmentConfig)
elif config_type == 'testing':
    app.config.from_object(TestingConfig)
elif config_type == 'production':
    app.config.from_object(ProductionConfig)

with app.app_context():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        add_user(username, email, password)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_or_email = request.form['user_or_email']
        password = request.form['password']

        con = get_db_connection()
        cur = con.cursor()

        cur.execute('SELECT * FROM user WHERE username = ? OR email = ?', (user_or_email, user_or_email))
        user = cur.fetchone()
        con.close()

        if user and user['password'] == password:
            session['logged_in'] = True
            session['username'] = user['username']
            return redirect(url_for('matrix'))
        else:
            error = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/matrix')
def matrix():
    if 'logged_in' in session:
        username = session['username']
        return render_template('matrix.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/start_game')
def start_game():
    if 'logged_in' in session:
        return redirect(url_for('matrix'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=5001)
