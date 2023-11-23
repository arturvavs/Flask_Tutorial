from website import create_app #Website é uma pasta 'package', então importamos a função de inicialização da aplicação Flask

app = create_app()

if __name__ == '__main__': #Essas linha diz o seguinte: 'Apenas se executarmos esse arquivo 'main.py', a linha app.run(debug=True) será executada
    app.run(debug=True)    #