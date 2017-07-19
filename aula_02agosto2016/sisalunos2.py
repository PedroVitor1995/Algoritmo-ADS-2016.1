def main():
	menu = ' 1 - Novo \n 2 - Listar Alunos \n 3 - Remover \n '\
		'4 - Listar Cursos \n ' \
		'0 - Sair \n OP >> '
		
	#print menu
	#bd_alunos =  #[] #list()
	bd_alunos = inicializar()
	bd_cursos = inicializar_cursos()

	
	while True:
		opcao = input(menu)
		
		if opcao == 1:
			#pedir os dados
			aluno = novo_aluno(bd_cursos)
			bd_alunos.append(aluno)
			print 'Aluno cadastrado com sucesso!'
		elif opcao == 2:
			listar_alunos(bd_alunos, bd_cursos)
		elif opcao == 3:
			remover_aluno(bd_alunos)
		elif opcao == 4:
			listar_cursos(bd_cursos)
		elif opcao == 0:
			finalizar(bd_alunos)
			break
		else:
			print 'opcao invalida.'

	print 'Finalizado.'


def inicializar_cursos():

	file = open('cursos.txt', 'r')
	cursos = []
	
	if len(file.readlines()) == 0:
		cursos = importar_cursos()
	else:
		file.seek(0) #para o inicio do arquivo novamente
		for linha in file:
			cursos.append(eval(linha))
	file.close()
	return cursos


def importar_cursos():
	file = open('cursos_para_importacao_inicial.txt', 'r')
	file_cursos = open('cursos.txt', 'a')
	cursos = []
	for l in file:
		dados = l.strip().split(',')
		sigla = dados[0]
		nome = dados[1]
		modalidade = dados[2]
		curso = {'sigla':sigla, 'nome': nome, 'modalidade': modalidade}
		cursos.append(curso)
		file_cursos.write(str(curso) + '\n')


	return cursos


def inicializar():
	arquivo_alunos = open('alunos.txt','r')
	linhas = arquivo_alunos.readlines()
	alunos = []
	for linha in linhas:
		alunos.append(eval(linha))
	arquivo_alunos.close()

	return alunos

def finalizar(lista):
	arquivo = open('alunos.txt', 'w')
	
	for aluno in lista:
		arquivo.write(str(aluno) + '\n')
	arquivo.close()


def novo_aluno(cursos):
	nome = raw_input('Nome:  ')
	sexo = raw_input('Sexo M-F: ')
	idade = input('Idade: ')
	listar_cursos(cursos)
	
	sigla_curso = raw_input('Sigla curso: ')
	while not sigla_valida(sigla_curso, cursos):
		print 'Curso Invalido.'
		sigla_curso = raw_input('Sigla curso: ')

	aluno = {'nome': nome, 'idade': idade, 'sexo':sexo, 'sigla_curso': sigla_curso} 
	
	return aluno

def listar_alunos(bd_alunos, cursos):
	print 'Alunos Cadastrados (%d)' % len(bd_alunos)
	#for item in bd_alunos:
	#	print item['nome'], item['idade'], item['sexo']
	for i in range(len(bd_alunos)):
		curso = obter_curso_por_sigla(bd_alunos[i]['sigla_curso'], cursos)
		print i, bd_alunos[i]['nome'], bd_alunos[i]['idade'], bd_alunos[i]['sexo'], \
			curso['sigla'], curso['nome']

def obter_curso_por_sigla(sigla, cursos):
	for curso in cursos:
		if sigla == curso['sigla']:
			return curso


def listar_cursos(bd_cursos):
	print 'Cursos cadastrados (%d)' % len(bd_cursos)
	for i in bd_cursos:
		print "%s - %s - %s" % (i['sigla'], i['nome'], i['modalidade'])

def sigla_valida(sigla, cursos):
	for curso in cursos:
		if sigla == curso['sigla']:
			return True

	return False

def remover_aluno(bd_alunos):
	listar_alunos(bd_alunos)
	posicao = input('Qual indice? ')
	#del bd_alunos[posicao]
	removido = bd_alunos.pop(posicao)
	print 'Aluno: ', removido['nome'], ' removido.'



if __name__ == '__main__':
	main()