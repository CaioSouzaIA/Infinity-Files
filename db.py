import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",          # ajuste conforme seu usuário
        password="Aluno123", # ajuste conforme sua senha
        database="loja"
    )