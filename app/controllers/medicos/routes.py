from flask import render_template, flash, redirect, request
from app import app

from app.models.models import Medico, db

from .forms import InsereMedicoForm


@app.route('/medicos',methods=['GET'])
def lista_medicos():
    dados = Medico.query.all()
    return render_template('medicos.html', dados = dados)

@app.route('/medicosadd',methods=['GET'])
def add_medico_get():
    form = InsereMedicoForm()
    return render_template('add_medico.html', form = form)

@app.route('/medicosadd',methods=['POST'])
def add_medico_post():
    form = InsereMedicoForm(request.form)
    if form.validate_on_submit():
        novo_medico = Medico(nome=form.nome.data,especialidade=form.especialidade.data)
        db.session.add(novo_medico)
        db.session.commit()
        flash('Médico cadastrado com sucesso','success')
    else:
        flash('Erro nos dados.'+str(form.errors),'danger')
    return redirect('/medicos')
    
@app.route('/medicosedit/<_id>',methods=['GET'])
def edit_medico_get(_id):
    m = Medico.query.filter_by(id=_id).first()
    form = InsereMedicoForm(obj=m)
    return render_template('edit_medico.html', form = form, _id=_id)

@app.route('/medicosedit/<_id>',methods=['POST'])
def edit_medico_post(_id):
    form = InsereMedicoForm(request.form)
    m = Medico.query.filter_by(id=_id).first()
    if form.validate_on_submit():
        form.populate_obj(m)
        db.session.commit()
        flash('Alterado com sucesso!','success')
    else:
        flash('Nao alterado, revise os dados.'+str(form.errors),'danger')
    return redirect('/medicos')


@app.route('/medicosview/<_id>',methods=['GET'])
def view_medico_get(_id):
    m = Medico.query.filter_by(id=_id).first()
    return render_template('view_medico.html', d = m)


@app.route('/medicosdel/<_id>',methods=['GET','POST'])
def del_medico(_id):
    m = Medico.query.filter_by(id=_id).first()
    db.session.delete(m)
    db.session.commit()
    flash('{} excluído com sucesso.'.format(m.nome),'success')
    return redirect('/medicos')