from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask(__name__)

conexao = mysql.connector.connect(host="localhost", port="3406", user="root", password="" , database="academia_flask")
cursor = conexao.cursor(dictionary=True)


@app.route('/') 
def index():
    cursor.execute("SELECT COUNT(nome) AS total_alunos FROM alunos")
    soma_alunos = cursor.fetchone()

    return render_template("index.html", soma_alunos=soma_alunos['total_alunos'])

@app.route("/alunos")
def alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    return render_template("alunos.html", alunos=alunos)

@app.route("/treinos")
def treinos():
    cursor.execute("SELECT * FROM treinos")
    treinos = cursor.fetchall()
    
    return render_template("treinos.html", treinos=treinos)


@app.route('/cast-aluno')
def cast_aluno():
    return render_template("cast-aluno.html")

@app.route("/salvar-aluno", methods=["POST"])
def salvar_aluno():
    nome = request.form["nome"]
    idade = request.form["idade"]
    plano = request.form["plano"]

    sql = "INSERT INTO alunos (nome, idade, plano) VALUES (%s, %s, %s)"
    val = (nome, idade, plano)

    cursor = conexao.cursor(dictionary = True)
    cursor.execute(sql, val)
    conexao.commit()

    return redirect("/alunos")


@app.route('/cast-treino')
def cast_treino():
    return render_template("cast-treino.html")

@app.route("/salvar-treino", methods=["POST"])
def salvar_treino():
    nome = request.form["nome"]
    nivel = request.form["nivel"]
    duracao = request.form["duracao"]

    sql = "INSERT INTO treinos (nome, nivel, duracao) VALUES (%s, %s, %s)"
    val = (nome, nivel, duracao)

    cursor = conexao.cursor(dictionary = True)
    cursor.execute(sql, val)
    conexao.commit()

    return redirect("/treinos")

@app.route("/deletar-treino/<int:id>")
def deletar_treino(id):
    sql = "DELETE FROM treinos WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()
    return redirect("/treinos")

@app.route("/deletar-aluno/<int:id>")
def deletar_aluno(id):
    sql = "DELETE FROM alunos WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conexao.commit()
    return redirect("/alunos")

@app.route("/editar-alunos/<int:id>")
def editar_aluno(id):
    sql = "SELECT * FROM alunos WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    aluno = cursor.fetchone()

    return render_template("editar-alunos.html", aluno=aluno)

@app.route("/atualizar-aluno/<int:id>", methods=["POST"])
def atualizar_aluno(id):
    nome = request.form["nome"]
    idade = request.form["idade"]
    plano = request.form["plano"]

    sql = "UPDATE alunos SET nome = %s, idade = %s, plano = %s WHERE id = %s"
    val = (nome, idade, plano, id)

    cursor = conexao.cursor(dictionary = True)
    cursor.execute(sql, val)
    conexao.commit()

    return redirect("/alunos")

@app.route("/editar-treino/<int:id>")
def editar_treino(id):
    sql = "SELECT * FROM treinos WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    treino = cursor.fetchone()

    return render_template("editar-treino.html", treino=treino)

@app.route("/atualizar-treino/<int:id>", methods=["POST"])
def atualizar_treino(id):
    nome = request.form["nome"]
    nivel = request.form["nivel"]
    duracao = request.form["duracao"]

    sql = "UPDATE treinos SET nome = %s, nivel = %s, duracao = %s WHERE id = %s"
    val = (nome, nivel, duracao, id)

    cursor = conexao.cursor(dictionary = True)
    cursor.execute(sql, val)
    conexao.commit()

    return redirect("/treinos")

if __name__ == "__main__":
    app.run(debug=True)