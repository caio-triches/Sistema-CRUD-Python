from flask import Flask, render_template, request, redirect, url_for
from db import db
from models import Treino, Alunos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///academia.db"
db.init_app(app)


@app.route('/') 
def index():
    return render_template("index.html")

    
@app.route("/treinos")
def treinos():
    treinos = db.session.query(Treino).all()
    return render_template("treinos.html", treino=treinos)

@app.route("/cast-treino", methods=["POST", "GET"])
def registrar():
    if request.method == "GET":
        return render_template("cast-treino.html")
    elif request.method == "POST":
        nome = request.form["nome"]
        nivel = request.form["nivel"]
        duracao = request.form["duracao"]

        new_trainer = Treino(nome=nome, nivel=nivel, duracao=duracao)
        db.session.add(new_trainer)
        db.session.commit()

        return redirect(url_for('treinos'))

@app.route("/deletar/<int:id>")
def deletar(id):
    treino = db.session.query(Treino).filter_by(id=id).first()
    db.session.delete(treino)
    db.session.commit()

    return redirect(url_for('treinos'))

@app.route("/editar-treino/<int:id>", methods=['GET', 'POST'])
def editar(id):
    treino = db.session.query(Treino).filter_by(id=id).first()
    if request.method == 'GET':
        return render_template("/editar-treino.html", treino=treino)
    elif request.method == 'POST':
        nome = request.form['nome']
        nivel = request.form['nivel']
        duracao = request.form['duracao']

        treino.nome = nome
        treino.nivel = nivel
        treino.duracao = duracao

        db.session.commit()

        return redirect(url_for('treinos'))
    

@app.route("/alunos")
def alunos():
    alunos = db.session.query(Alunos).all()
    return render_template("alunos.html", alunos=alunos)

@app.route('/cast-aluno', methods=['GET', 'POST'])
def registrar_aluno():
    if request.method == "GET":
        return render_template("cast-aluno.html")
    elif request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]
        plano = request.form["plano"]

        new_user = Alunos(nome=nome, idade=idade, plano=plano)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('alunos'))
    
@app.route("/deletar-alunos/<int:id>")
def deletar_alunos(id):
    alunos = db.session.query(Alunos).filter_by(id=id).first()
    db.session.delete(alunos)
    db.session.commit()

    return redirect(url_for('alunos'))

@app.route("/editar-alunos/<int:id>", methods=['GET', 'POST'])
def editar_alunos(id):
    alunos = db.session.query(Alunos).filter_by(id=id).first()
    if request.method == 'GET':
        return render_template("/editar-alunos.html", alunos=alunos)
    elif request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        plano = request.form['plano']

        alunos.nome = nome
        alunos.idade = idade
        alunos.plano = plano

        db.session.commit()

        return redirect(url_for('alunos'))
    



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)