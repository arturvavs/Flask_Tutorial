from flask import Blueprint
import cx_Oracle
import json

models = Blueprint('models', __name__)

class Oracle():
    def __init__(self):
        self.un = 'tasy'
        self.cs = '172.27.27.6:1521/tasyfh.saocamilo.corp'
        self.pw = 'aloisk'
        self.connection = None
        self.sql = None

    def user_login(self,nm_usuario):
        connection = cx_Oracle.connect(user=self.un, password=self.pw, dsn=self.cs)
        validation = False
        new_nm_usuario = nm_usuario.upper()
        sql = (f"SELECT NM_USUARIO FROM USUARIO WHERE NVL(DS_LOGIN,NM_USUARIO) = '{new_nm_usuario}'")
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    row = cursor.fetchone()
                    if row:
                        validation = True
                        return validation
                    else:
                        validation = False
                        return validation
            except cx_Oracle.Error as error:
                print('Erro ao executar funcao:', error)
                return None
        