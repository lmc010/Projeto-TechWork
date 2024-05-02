from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Alunos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    email = db.Column(db.String(100))
    semestre = db.Column(db.Integer)

    def __init__(self, nome, cidade, email, semestre):
        self.nome = nome
        self.cidade = cidade
        self.email = email
        self.semestre = semestre