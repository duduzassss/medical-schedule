from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class InserePacienteForm(FlaskForm):
    nome     = StringField('Nome', validators=[InputRequired(), Length(min=3)])
    telefone = StringField('Telefone',validators=[InputRequired(),Length(min=6)])
    cpf      = StringField('CPF',validators=[InputRequired(),Length(min=11,max=11)])
    senha    = PasswordField('Senha',validators=[InputRequired(),Length(min=6)])
    enviar   = SubmitField('Enviar')