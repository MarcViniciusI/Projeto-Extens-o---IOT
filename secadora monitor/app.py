import os
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from dotenv import load_dotenv
from firebase_admin import auth as firebase_auth
from auth import User
from data import get_latest_temperature, get_temperature_history, generate_insights


# Carregar as variáveis de ambiente
load_dotenv()

# Configuração da aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')#Segurança de Dados Sensíveis: O .env é o local ideal para armazenar dados

# Configuração do Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
@login_required
def dashboard():
    latest_temp = get_latest_temperature()
    return render_template('dashboard.html', latest_temp=latest_temp)


@app.route('/history')
@login_required
def history():
    temp_history = get_temperature_history()
    return render_template('history.html', temp_history=temp_history)


@app.route('/insights')
@login_required
def insights():
    insight_data = generate_insights()
    return render_template('insights.html', insight_data=insight_data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.authenticate(username, password)
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid username or password')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        try:
            user = firebase_auth.create_user(
                email=email,
                password=password
            )
            flash('Usuário registrado com sucesso!')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Erro ao registrar usuário: {e}')
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
