from flask import Flask

#ESTRUTURA DA APLICAÇÃO FLASK
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'root@123' #Criptografa os dados de cookies do website

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app