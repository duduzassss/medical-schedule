from app import db
from flask_login import UserMixin

class Medico(db.Model):
    __tablename__ = 'medicos'
    id   = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250))
    especialidade = db.Column(db.String(250))


    def __repr__(self):
        return '<Medico: {} /{}>'.format(self.nome, self.especialidade)

    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

class Paciente(db.Model, UserMixin):
    __tablename__ = 'pacientes'
    id       = db.Column(db.Integer, primary_key=True)
    nome     = db.Column(db.String(250))
    telefone = db.Column(db.String(50))
    cpf      = db.Column(db.String(20))
    password_hash = db.Column(db.String(250))
    
    def __repr__(self):
        return '<Paciente: {}>'.format(self.nome)

    def __init__(self, nome,telefone,cpf,password):
        self.nome     = nome
        self.telefone = telefone
        self.cpf      = cpf
        self.password_hash = generate_password_hash(password)

class Consulta(db.Model, UserMixin):
    __tablename__ = 'consultas'
    id       = db.Column(db.Integer,primary_key=True) 
    medico   = db.Column(db.String(250))
    paciente = db.Column(db.String(250))
    horario  = db.Column(db.Integer)
    data     = db.Column(db.Date())

    def __repr__(self):
        return '<Consulta: {}>'.format(self.nome)