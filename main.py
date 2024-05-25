from flask import Flask, render_template,request,redirect,flash,session
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'PI01'

#caminhos definidos para as páginas
@app.route("/")
def cadastro():

    return render_template('cadastro.html')


@app.route('/login')
def index():

    return render_template('index.html')


@app.route('/loginrequisitante')
def loginrequisitante():

    return render_template('loginrequisitante.html')


@app.route('/loginoperador')
def loginoperador():

    return render_template('loginoperador.html')

@app.route('/layout')
def layout():

    return render_template('layout.html')

#verificação de usuário e senha para requisitante
@app.route("/acessorequisitante", methods=['POST'])
def acessorequisitante():
    email = request.form.get('usuariorequisitante')
    senha = request.form.get('senharequisitante')

    with open('requisitante.json') as requisitante_json:
        listaDeUsuarios = json.load(requisitante_json)
        cont = 0
        for usuario in listaDeUsuarios:
            cont += 1

            if email == usuario['email'] and senha == usuario['senha']:
                return redirect('/layout')
            if cont >= len(listaDeUsuarios):
                flash('Email ou senha incorretos.')
                return redirect('/loginrequisitante')

#verificação de usuário e senha para operador 

@app.route("/acessooperador", methods=['POST'])
def acessooperador():
    usuario = request.form.get('usuariooperador')
    senha = request.form.get('senhaoperador')

    if usuario == 'grupo10' and senha == '123':
        return redirect('/layout')
    else:
        return redirect('/loginoperador')
    
#Enviar os dados dos cadastros de  requisitante para o JSON


@app.route("/requisitantecadastro", methods=['POST'])
def requisitantecadastro():

    email = request.form.get('emailrequisitante')
    nome = request.form.get('nomerequisitante')
    senha = request.form.get('senharequisitante')

    with open('requisitante.json') as requisitante_json:
        listaDeUsuarios = json.load(requisitante_json)
        for usuario in listaDeUsuarios:
            if usuario['email'] == email:
                flash('Email já cadastrado.')
                return redirect('/loginrequisitante')
            
    user = [
        {   
            "email": email,
            "nome": nome,
            "senha": senha,
        }
    ]

    novalista = listaDeUsuarios + user

    with open("requisitante.json", 'w') as requisitante_json:
        json.dump(novalista, requisitante_json, indent=4)

    return redirect('/loginrequisitante')





if __name__ in '__main__':
    app.run( debug=True )