from flask import render_template, flash, redirect, request
from app import app

from app.models.models import Paciente, db

from .forms import InserePacienteForm


@app.route('/pacientes',methods=['GET'])
def lista_pacientes():
    dados = Paciente.query.all()
    return render_template('pacientes.html', dados = dados)

@app.route('/pacientesadd',methods=['GET'])
def add_paciente_get():
    form = InserePacienteForm()
    return render_template('add_paciente.html', form = form)

@app.route('/pacientesadd',methods=['POST'])
def add_paciente_post():
    form = InserePacienteForm(request.form)
    if form.validate_on_submit():
        novo_paciente = Paciente(nome=form.nome.data,
            telefone=form.telefone.data,
            cpf=form.cpf.data,
            password = form.senha.data)
        db.session.add(novo_paciente)
        db.session.commit()
        flash('Paciente cadastrado com sucesso','success')
    else:
        flash('Erro nos dados.'+str(form.errors),'danger')
    return redirect('/pacientes')
    
@app.route('/pacientesedit/<_id>',methods=['GET'])
def edit_paciente_get(_id):
    p = Paciente.query.filter_by(id=_id).first()
    form = InserePacienteForm(obj=p)
    return render_template('edit_paciente.html', form = form, _id=_id)

@app.route('/pacientesedit/<_id>',methods=['POST'])
def edit_paciente_post(_id):
    form = InserePacienteForm(request.form)
    p = Paciente.query.filter_by(id=_id).first()
    if form.validate_on_submit():
        form.populate_obj(p)
        db.session.commit()
        flash('Paciente alterado com sucesso.','success')
    else:
        flash('Nao alterado, revise os dados.'+str(form.errors),'danger')
    return redirect('/pacientes')


@app.route('/pacientesview/<_id>',methods=['GET'])

def view_paciente_get(_id):
    p = Paciente.query.filter_by(id=_id).first()
    return render_template('view_paciente.html', d = p)

@app.route('/pacientesdel/<_id>',methods=['GET'])

def del_paciente_get(_id):
    p = Paciente.query.filter_by(id=_id).first()
    return render_template('del_paciente.html', d = p)

@app.route('/pacientesdel/<_id>',methods=['POST'])

def del_paciente_post(_id):
    p = Paciente.query.filter_by(id=_id).first()
    db.session.delete(p)
    db.session.commit()
    flash('Paciente excluído com sucesso.','success')
    return redirect('/pacientes')