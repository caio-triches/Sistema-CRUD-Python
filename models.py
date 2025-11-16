from db import db

class Treino(db.Model):
    __tablename__ = "treinos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=True)
    nivel = db.Column(db.String(50), nullable=False)
    duracao = db.Column(db.Integer)

    def __repr__(self):
        return f"<{self.nome}>"
    

class Alunos(db.Model):
    __tablename__ = "Alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    plano = db.Column(db.String(100), nullable=False)