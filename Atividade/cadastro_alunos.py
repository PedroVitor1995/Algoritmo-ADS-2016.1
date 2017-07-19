def main():
	menu = (' 1 - Cadastrar \n 2 - Listar \n 3 - Remover \n 0 - Sair \n Opcao: ')
	alunos = []
	while True:
		opcao = input(menu)
		if opcao == 1:
			cadastrar(alunos)
			print ('Aluno cadastrado com sucesso!')
		elif opcao == 2:
			listar(alunos)
		elif opcao == 3:
			remover(alunos)
		elif opcao == 0:
			print('Saindo do programa')
			reposta = raw_input('Dejesa realmente sair S/N: ')
			if reposta == 'N' or reposta == 'n':
				continue
			else:
				break
		else:
			print ('Opcao invalida.')

	print ('Programa finalizado.')
def cadastrar(alunos):
	aluno = {}
	aluno['Nome'] = raw_input('Nome: ')
	while True:
		aluno['Idade'] = input('Idade: ')
		if aluno['Idade'] > 0:
			break
		else:
			continue
	while True:
		aluno['Sexo'] = raw_input('Sexo M/F: ')
		if aluno['Sexo'] == 'F' or aluno['Sexo'] == 'M' or aluno['Sexo'] == 'f' or aluno['Sexo'] == 'm':
			break
		else:
			continue
	alunos.append(aluno)
	return alunos
def listar(alunos):
	print ('Alunos Cadastrados (%d)') % len(alunos)
	for i in range(len(alunos)):
		print alunos[i]
def remover(alunos):
	listar(alunos)
	nome = raw_input('Digite o nome do aluno que deseja remover: ')
	quantidade = 0
	for i in range(len(alunos)):
		if alunos[i]['Nome'] == nome:
			quantidade += 1
	if quantidade == 1:
		for i in range(len(alunos)):
			if alunos[i]['Nome'] == nome:
				del alunos[i]
				print ('Aluno %s removido com sucesso!')%(nome)
				break
	else:
		idade = input('Digite a idade do aluno que dejesa remover: ')
		for i in range(len(alunos)):
			if alunos[i]['Nome'] == nome and alunos[i]['Idade'] == idade:
				del alunos[i]
				print ('Aluno %s com idade %d removido com sucesso!') % (nome,idade)
				break
if __name__ == '__main__':
	main()