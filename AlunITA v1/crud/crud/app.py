#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db2.sqlite'

db3 = SQLAlchemy(app)

class NovoUsuarioCadastrado(db3.Model):
	__tablename__ = 'novoUsuario'
	_id = db3.Column(db3.Integer, primary_key=True, autoincrement=True)
	nomeNovoUsu = db3.Column(db3.String)
	sobrenomeNovoUsu = db3.Column(db3.String)
	nomeusuarioNovoUsu = db3.Column(db3.String)
	senhaNovoUsu = db3.Column(db3.String)
	emailNovoUsu = db3.Column(db3.String)
	cursoNovoUsu = db3.Column(db3.String)
	anoformacaoNovoUsu = db3.Column(db3.Integer)
	materia1 = db3.Column(db3.String)
	materia2 = db3.Column(db3.String)
	materia3 = db3.Column(db3.String)
	materia4 = db3.Column(db3.String)
	materia5 = db3.Column(db3.String)
	materia6 = db3.Column(db3.String)
	materia7 = db3.Column(db3.String)
	materia8 = db3.Column(db3.String)
	
	def __init__(self, novonome, sobrenome, nomeusuario, novasenha, email, curso, anoformacao, 
		materia1, materia2, materia3, materia4, materia5, materia6, materia7, materia8):
		self.nomeNovoUsu = novonome
		self.sobrenomeNovoUsu = sobrenome
		self.nomeusuarioNovoUsu = nomeusuario
		self.senhaNovoUsu = novasenha
		self.emailNovoUsu = email
		self.cursoNovoUsu = curso
		self.anoformacaoNovoUsu = anoformacao
		self.materia1 = materia1
		self.materia2 = materia2
		self.materia3 = materia3
		self.materia4 = materia4
		self.materia5 = materia5
		self.materia6 = materia6
		self.materia7 = materia7
		self.materia8 = materia8


db3.create_all()


@app.route("/")
@app.route("/login")
def home():
	return render_template("login.html")

@app.route("/")
@app.route("/cadastrousuario")
def cadastrar():
	return render_template("cadastrousuario.html")

@app.route("/")
@app.route("/principal")
def principal():
	return render_template("principal.html")

p = NovoUsuarioCadastrado("", "", "", "", "", "", "", 
													"", "", "", "", "", "", "", "")

usuarioProcurado = NovoUsuarioCadastrado("", "", "", "", "", "", "",
										"", "", "", "", "", "", "", "")

@app.route("/cadastrandousuario", methods=['GET', 'POST'])
def cadastro():
	if request.method == "POST":
		nome = (request.form.get("first_name"))
		sobrenome = (request.form.get("last_name"))
		nomeusuario = (request.form.get("usuario_valido"))
		senha = (request.form.get("password"))
		email = (request.form.get("email_inline"))
		curso = (request.form.get("curso-select"))
		anoformacao = (request.form.get("anoformacao-select"))
		materia1 = (request.form.get("nome-materia1"))
		materia2 = (request.form.get("nome-materia2"))
		materia3 = (request.form.get("nome-materia3"))
		materia4 = (request.form.get("nome-materia4"))
		materia5 = (request.form.get("nome-materia5"))
		materia6 = (request.form.get("nome-materia6"))
		materia7 = (request.form.get("nome-materia7"))
		materia8 = (request.form.get("nome-materia8"))

		if nome and sobrenome and nomeusuario and senha and email and curso and anoformacao and materia1 and materia2 and materia3 and materia4 and materia5 and materia6 and materia7 and materia8:
			global p
			p = NovoUsuarioCadastrado(nome, sobrenome, nomeusuario, senha, email, curso, anoformacao, materia1, materia2, materia3, materia4, materia5, materia6, materia7, materia8)
			db3.session.add(p)
			db3.session.commit()
			
			return render_template("principal.html", usuario=p)

	return redirect(url_for("cadastrar"))

@app.route('/autenticar', methods=['POST'])
def autenticar():
	usuario = (request.form.get("usuario"))
	senha = (request.form.get("senha"))

	global usuarioProcurado
	# global usuarioProcurado2
	usuarioProcurado = NovoUsuarioCadastrado.query.filter_by(nomeusuarioNovoUsu=usuario).first()
	# usuarioProcurado2 = usuarioProcurado
	if usuarioProcurado:
		if senha == usuarioProcurado.senhaNovoUsu:
			return render_template("principal.html", usuario=usuarioProcurado)
		else:
			return render_template("login.html")
	else:
			return render_template("login.html")

@app.route('/notas')
def Notas():
	global usuarioProcurado
	return render_template('notas.html', titulo='Notas', usuario=usuarioProcurado)

@app.route('/formularionota')
def formularionota():
	global usuarioProcurado
	return render_template('formularionota.html', titulo='Adicionar nova nota', usuario=usuarioProcurado)

@app.route("/lista")
def lista():
	usuarios = NovoUsuarioCadastrado.query.all()
	return render_template("lista.html", usuarios=usuarios)

# @app.route("/atualizar/<int:id>", methods=['GET', 'POST'])
# def atualizar(id):
# 	pessoa = Pessoa.query.filter_by(_id=id).first()
# 	if request.method == "POST":
# 		nome = (request.form.get("nome"))
# 		rua = (request.form.get("rua"))
# 		numero = (request.form.get("numero"))
# 		bairro = (request.form.get("bairro"))
# 		cidade = (request.form.get("cidade"))
# 		estado = (request.form.get("estado"))
# 		fone = (request.form.get("fone"))
# 		email = (request.form.get("email"))

# 		if nome and rua and numero and bairro and cidade and estado and fone and email:
# 			pessoa.nome = nome
# 			pessoa.rua= rua
# 			pessoa.numero = numero
# 			pessoa.bairro = bairro
# 			pessoa.cidade = cidade
# 			pessoa.estado = estado
# 			pessoa.fone = fone
# 			pessoa.email = email
# 			db3.session.commit()

# 	return render_template("atualizar.html", pessoa=pessoa)

# @app.route("/excluir/<int:id>")
# def excluir(id):
# 	pessoa = Pessoa.query.filter_by(_id=id).first()

# 	db3.session.delete(pessoa)
# 	db3.session.commit()
	
# 	pessoas = Pessoa.query.all()
# 	return render_template("lista.html", pessoas=pessoas)





if __name__ == "__main__":
	# with app.app_context():
	# 	msg = Message(subject="Hello",
	# 								sender=app.config.get("isabelle.ferreira3000@gmail.com"),
	# 								recipients=["isabelle.ferreira3000@gmail.com"],
	# 								body="this is a test")
	# 	mail.send(msg)
	app.run(debug=True)