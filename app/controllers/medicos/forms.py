from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, Email, Length,  ValidationError, EqualTo


class InsereMedicoForm(FlaskForm):
    nome   = StringField('Nome', validators=[InputRequired(), Length(min=3)])
    especialidade = StringField('Especialidade',validators=[InputRequired(),Length(min=4)])
    enviar = SubmitField('Enviar')
