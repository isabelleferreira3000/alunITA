from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'carniceria'

class NotaMateria:
	def __init__(self, nome, media1, media2, mediafinal):
		self.nome = nome
		self.media1 = media1
		self.media2 = media2
		self.mediafinal = mediafinal
		

#abortar essa classe
class Usuario:
	def __init__(self, idd, nome, senha):
		self.idd = idd
		self.nome = nome
		self.senha = senha

class NovoUsuarioCadastrado:
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


NovoUsu1 = NovoUsuarioCadastrado('Lívia', 'Pimentel', 'livinha100canela', 'pacocandeaveia', 'liviafragoso.pi@gmail.com', 'AER', '2020',
	'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx')
NovoUsu2 = NovoUsuarioCadastrado('Talita', 'Castro', 'talitamejeira', 'soudomej', 'talitacastro126@gmail.com', 'MEC', '2020', 
	'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx')
NovoUsu3 = NovoUsuarioCadastrado('Rafaella', 'Bambokian', 'bambokian', 'carniceria', 'rafaellabambokian@gmail.com', 'COMP', '2020',
	'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx')

listaUsuariosCadastrados = [NovoUsu1, NovoUsu2, NovoUsu3]
listaGambi = [NovoUsu1]
listamateriasUsuario = []
      			
# substituir por banco de dados
usuarios = {NovoUsu1.nomeusuarioNovoUsu: NovoUsu1, NovoUsu2.nomeusuarioNovoUsu: NovoUsu2, NovoUsu3.nomeusuarioNovoUsu: NovoUsu3}

# Renderização de páginas
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
	if request.form['usuario'] in usuarios:
		usuarioLogando = usuarios[request.form['usuario']]
		if usuarioLogando.senhaNovoUsu ==  request.form['senha']:
			session['usuario_logado'] = usuarioLogando.nomeusuarioNovoUsu
			# gambiarra
			listaGambi.append(usuarioLogando)

			return redirect('/principal')
			flash(usuarioLogando.nomeNovoUsu + ' logado com sucesso.') #ta bugandoooo
		else:
			flash('Senha incorreta. Tente novamente!')
			return redirect('/login')
	else:
		flash(request.form['usuario'] + ' não logado. Tente novamente!')
		return redirect('/login')

@app.route('/principal')
def principal():
	ultimoEle = len(listaGambi)-1 #AAAA
	return render_template('principal.html', nomeLogin = listaGambi[ultimoEle].nomeNovoUsu + ' ' + listaGambi[ultimoEle].sobrenomeNovoUsu,
		cursoLogin = listaGambi[ultimoEle].cursoNovoUsu, semestreLogin ='Turma ' + listaGambi[ultimoEle].anoformacaoNovoUsu)

@app.route('/logout')
def logout():
	session['usuario_logado'] = None
	flash('Nenhum usuário logado.')
	return redirect('/login')

@app.route('/cadastrousuario')
def cadastropessoais():
	return render_template('cadastrousuario.html')

@app.route('/cadastrandousuario', methods=['POST',])
def salvardadospessoais():
	primeiroNome = request.form['first_name']
	ultimoNome = request.form['last_name']
	novoUsuario = request.form['usuario_valido']
	novaSenha = request.form['password']
	novoEmail = request.form['email_inline']
	cursoUsu = request.form['curso-select']
	anoformacaoUsu = request.form['anoformacao-select']
	materia1 = request.form['nome-materia1']
	materia2 = request.form['nome-materia2']
	materia3 = request.form['nome-materia3']
	materia4 = request.form['nome-materia4']
	materia5 = request.form['nome-materia5']
	materia6 = request.form['nome-materia6']
	materia7 = request.form['nome-materia7']
	materia8 = request.form['nome-materia8']

	NovoUsuInserido = NovoUsuarioCadastrado(primeiroNome, ultimoNome, novoUsuario, novaSenha, novoEmail, cursoUsu, anoformacaoUsu,
		materia1, materia2, materia3, materia4, materia5, materia6, materia7, materia8)
	listaUsuariosCadastrados.append(NovoUsuInserido)
	ultimoEle = len(listaUsuariosCadastrados)-1
	return render_template('principal.html', 
		nomeLogin = listaUsuariosCadastrados[ultimoEle].nomeNovoUsu + ' ' + listaUsuariosCadastrados[ultimoEle].sobrenomeNovoUsu,
		cursoLogin = listaUsuariosCadastrados[ultimoEle].cursoNovoUsu, semestreLogin ='Turma ' + listaUsuariosCadastrados[ultimoEle].anoformacaoNovoUsu)


@app.route('/notas')
def Notas():
	ultimoElem = len(listaUsuariosCadastrados)-1 #AAAA
	listam1 = NotaMateria(listaUsuariosCadastrados[ultimoElem].materia1, '0', '0', '0')
	listamateriasUsuario.append(listam1)
	listam2 = NotaMateria(listaUsuariosCadastrados[ultimoElem].materia2, '0', '0', '0')
	listamateriasUsuario.append(listam2)
	listam3 = NotaMateria(listaUsuariosCadastrados[ultimoElem].materia3, '0', '0', '0')
	listamateriasUsuario.append(listam3)
	listam4 = NotaMateria(listaUsuariosCadastrados[ultimoElem].materia4, '0', '0', '0')
	listamateriasUsuario.append(listam4)
	listam5 = NotaMateria(listaUsuariosCadastrados[ultimoElem].materia5, '0', '0', '0')
	listamateriasUsuario.append(listam5)
	listam6 = NotaMateria(listaUsuariosCadastrados[ultimoElem].materia6, '0', '0', '0')
	listamateriasUsuario.append(listam6)
	listam7 = NotaMateria(listaUsuariosCadastrados[ultimoElem].materia7, '0', '0', '0')
	listamateriasUsuario.append(listam7)
	listam8 = NotaMateria(listaUsuariosCadastrados[ultimoElem].materia8, '0', '0', '0')
	listamateriasUsuario.append(listam8)
	#listamateriasUsuario = [listam1, listam2, listam3, listam4, listam5, listam6, listam7, listam8] #antiga listam
	return render_template('notas.html', materias=listamateriasUsuario)

@app.route('/formularionota')
def formularionota():
	if 'usuario_logado' not in session or session['usuario_logado'] == None:
		return redirect('/login')
	return render_template('formularionota.html', materias=listamateriasUsuario)

@app.route('/adicionarnota', methods=['POST',])
def salvarnotas():
# def salvar():
	materiaNota = request.form['materia']
	# atividadeNota = request.form['atividade']
	valorNota = request.form['valor']
	porcentagemNota = request.form['porcentagem']
	# listamx = NotaMateria(materiaNota, valorNota, valorNota, valorNota)
	# listam.append(listamx)

	return redirect('/notas')



	





@app.route('/agenda')
def  agenda():
	return render_template('agenda.html')

@app.route('/lembretes')
def  lembretes():
	return render_template('lembretes.html')



# @app.route('/principal')
# def principal():
# 	return render_template('principal.html', nomeLogin=usuarios[request.form['usuario']], 
# 		cursoLogin=usuarios[request.form['usuario']], semestreLogin=usuarios[request.form['usuario']])

app.run(debug=True)