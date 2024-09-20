import os
from flask_login import UserMixin
import firebase_admin
from firebase_admin import credentials, auth

# Inicialize o Firebase com as credenciais
FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH')#Segurança de Dados Sensíveis: O .env é o local ideal para armazenar dados
cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)


class User(UserMixin):
    def __init__(self, uid, email):
        self.id = uid
        self.email = email

    @staticmethod
    def get(user_id):
        try:
            user = auth.get_user(user_id)
            return User(user.uid, user.email)
        except auth.AuthError:
            return None

    @staticmethod
    def authenticate(email, password):
        # A autenticação de senha deve ser feita no cliente, não no servidor
        # Aqui, apenas um exemplo de como obter o usuário pelo e-mail
        try:
            user = auth.get_user_by_email(email)
            return User(user.uid, user.email)
        except auth.AuthError:
            return None
