def main():
	titulo = '***** CAD-ALUNOS ***** \n '
	menu = titulo + '1 - Novo Aluno'\
		'\n 2 - Listar Alunos \n 0 - Sair \n opcao >> '
	
	#lista de alunos
	alunos = []

	while True:
		op = input(menu)

		if op == 1:
			alunos.append(novo_aluno())
		elif op == 2:
			listar_alunos(alunos)
		elif op == 0:
			break
		else:
			print 'opcao invalida'

def novo_aluno():
	nome = raw_input('Nome:  ')
	idade = input('Idade: ')
	sexo = raw_input('Sexo, M ou F: ')

	aluno = {'nome':nome, 'idade':idade, 'sexo':sexo}
	return aluno


def listar_alunos(alunos, ordem):
	print '\nListagem de alunos \n'
	print 'NOME \t\t IDADE \t SEXO'
	for aluno in alunos:
		nome = aluno['nome']
		idade = aluno['idade']
		sexo = aluno['sexo']
		print '%s \t %d \t %s' % (nome, idade, sexo)
	print '\n'



if __name__ == '__main__':
	main()