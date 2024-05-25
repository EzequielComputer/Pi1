from flask import Flask, render_template,request,redirect,flash,session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'PI01'


@app.route("/")
def index():

    return render_template('index.html')



@app.route('/loginrequisitante')
def loginrequisitante():

    return render_template('loginrequisitante.html')


@app.route("/acessorequisitante", methods=['POST'])
def acessorequisitante():
    usuario = request.form.get('usuariorequisitante')
    senha = request.form.get('senharequisitante')

    if usuario == 'grupo10' and senha == '123':
        return redirect('/layout')
    else:
        return redirect('/loginrequisitante')


@app.route('/layout')
def layout():

    return render_template('layout.html')










if __name__ in '__main__':
    app.run( debug=True )