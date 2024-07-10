from flask import Flask, render_template, request, redirect, url_for, session
from db import get_db_connection, init_db, add_user
import subprocess
import os
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from dotenv import load_dotenv  # Asegúrate de que esta importación es correcta

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configura la aplicación Flask para usar el archivo config.py
config_type = os.getenv('FLASK_CONFIG_TYPE', 'development')
if config_type == 'development':
    app.config.from_object(DevelopmentConfig)
elif config_type == 'testing':
    app.config.from_object(TestingConfig)
elif config_type == 'production':
    app.config.from_object(ProductionConfig)

# Inicializa la base de datos al iniciar la aplicación
with app.app_context():
    init_db()

# Rutas para registro, login, y juego
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

        # Buscar por nombre de usuario o correo electrónico
        cur.execute('SELECT * FROM user WHERE username = ? OR email = ?', (user_or_email, user_or_email))
        user = cur.fetchone()
        con.close()

        if user and user['password'] == password:
            session['logged_in'] = True
            session['username'] = user['username']
            return redirect(url_for('game'))
        else:
            error = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/game')
def game():
    if 'logged_in' in session:
        username = session['username']
        return render_template('game.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route('/tech')
def tech():
    return render_template('tech.html')

# Ruta para iniciar el juego con Pygame
@app.route('/start_game')
def start_game():
    if 'logged_in' in session:
        game_path = os.path.join('static', 'js', 'game.py')
        subprocess.Popen(["python3", game_path])
        return "El juego ha comenzado! Al finalizar vuelve por tus recompensas 🎆."
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=5000)  # Ejemplo de cambiar al puerto 5001

