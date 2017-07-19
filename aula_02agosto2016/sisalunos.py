def main():
	menu = ' 1 - Novo \n 2 - Listar \n 3 - Remover \n 0 - Sair \n OP >> '
		
	#print menu
	#bd_alunos =  #[] #list()
	bd_alunos = inicializar()

	
	while True:
		opcao = input(menu)
		
		if opcao == 1:
			#pedir os dados
			aluno = novo_aluno()
			bd_alunos.append(aluno)
			print 'Aluno cadastrado com sucesso!'
		elif opcao == 2:
			listar_alunos(bd_alunos)
		elif opcao == 3:
			remover_aluno(bd_alunos)
		elif opcao == 0:
			finalizar(bd_alunos)
			break
		else:
			print 'opcao invalida.'

	print 'Finalizado.'


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


def novo_aluno():
	nome = raw_input('Nome:  ')
	sexo = raw_input('Sexo M-F: ')
	idade = input('Idade: ')
	aluno = {'nome': nome, 'idade': idade, 'sexo':sexo} 
	return aluno

def listar_alunos(bd_alunos):
	print 'Alunos Cadastrados (%d)' % len(bd_alunos)
	#for item in bd_alunos:
	#	print item['nome'], item['idade'], item['sexo']
	for i in range(len(bd_alunos)):
		print i, bd_alunos[i]['nome'], bd_alunos[i]['idade'], bd_alunos[i]['sexo']

def remover_aluno(bd_alunos):
	listar_alunos(bd_alunos)
	posicao = input('Qual indice? ')
	#del bd_alunos[posicao]
	removido = bd_alunos.pop(posicao)
	print 'Aluno: ', removido['nome'], ' removido.'



if __name__ == '__main__':
	main()