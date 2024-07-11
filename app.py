from flask import Flask, render_template, request, redirect, url_for, session
from db import get_db_connection, init_db, add_user
import subprocess
import os
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configurar la aplicación Flask para usar el archivo config.py
config_type = os.getenv('FLASK_CONFIG_TYPE', 'development')
if config_type == 'development':
    app.config.from_object(DevelopmentConfig)
elif config_type == 'testing':
    app.config.from_object(TestingConfig)
elif config_type == 'production':
    app.config.from_object(ProductionConfig)

# Inicializar la base de datos al iniciar la aplicación
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
            return redirect(url_for('game_pixi'))  # Cambiar a la ruta para el juego con Pixi.js
        else:
            error = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/game_pixi')  # Nueva ruta para el juego con Pixi.js
def game_pixi():
    if 'logged_in' in session:
        username = session['username']
        return render_template('game.html', username=username)  # Renderiza la plantilla game.html para Pixi.js
    else:
        return redirect(url_for('login'))

@app.route('/tech')
def tech():
    return render_template('tech.html')

# Nueva ruta para iniciar el juego con Pixi.js
@app.route('/start_game_pixi')
def start_game_pixi():
    if 'logged_in' in session:
        # Aquí podrías iniciar cualquier lógica adicional necesaria para el juego con Pixi.js
        return "El juego ha comenzado con Pixi.js! Al finalizar vuelve por tus recompensas 🎆."
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(port=5000)  # Ejemplo de cambiar al puerto 5001
