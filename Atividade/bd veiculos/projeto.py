from funcoes import *
def main():
	bd_veiculos = []
	bd_montadoras = []
	bd_veiculos += inicializar_veiculos()
	bd_montadoras += inicializar_montadoras()
	while True:
		print('------------------Opcoes----------------\n')
		print('1  - Cadastrar uma montadora ')
		if len(bd_montadoras) > 0:
			print('2  - Listar montadoras ')
			print('3  - Remover uma montadora ')
			print('4  - Editar uma montadora ')
			print('5  - Acrecentar um veiculo a lista ')
			if len(bd_veiculos) > 0:
				print('6  - Listar veiculo ja cadastrados ')
				print('7  - Apagar veiculo cadastrado ')
				print('8  - Editar veiculo cadastrado ')
		print('0  - Sair da aplicação.')

		opcao = int( input('Digite a opção desejada: ') )

		if opcao == 1:  #  - Cadastrar uma montadora
			limpar()
			print('\n----------Cadastrando montadora--------')
			nome_montadora = input('Digite o nome da montadora: ')
			nome_pais = input('Digite o nome do pais da montadora: ')
			if verifica_montadora(bd_montadoras, nome_montadora):
				bd_montadoras.append( acrecentar_montadora(nome_montadora, nome_pais) )
			else:
				print('Essa montadora ja esta cadastrada!!!')
	
		elif opcao == 2:#  - Listar montadoras 
			limpar()
			print('=============Mostrar montadoras=========')
			print('1  - todas')
			print('2  - pesquisa por nome')
			chave = int( input('Digite a opcao desejada: ') )
			if chave == 1:
				limpar()
				listar_montadoras(bd_montadoras)
			elif chave == 2:
				chave = input('Digite um nome para pesquisar: ')
				if pesquisa_valida(bd_montadoras, chave):
					limpar()
					pesquisar_nome_montadora(bd_montadoras, chave)
				else:
					print('A pesquisa nao encontrou nenhuma montadora.')

		elif opcao == 3:#  - Remover uma montadora 
			limpar()
			print('==========Removendo=========')
			listar_montadoras(bd_montadoras)
			id_montadora = int( input('Digite o id da montadora que deseja excluir da lista: ') )
			if( remover_montadora(bd_veiculos, bd_montadoras, id_montadora) ):
				print( 'Montadora {} removida com sucesso!'.format(id_montadora) )
			elif verifica_montadora(bd_montadoras, bd_montadoras[id_montadora]['nome']):
				print( 'A montadora {} nao existe!!!'.format(id_montadora) )
			else:
				print('A montadora {} nao pode ser removida pois contem veiculos nela ...'.format(bd_montadoras[id_montadora]['nome']))

		elif opcao == 4:#  - Editar uma montadora 
			limpar()
			listar_montadoras(bd_montadoras)
			id_montadora = int( input('Digite o id do montadora que deseja editar: ') )
			while True:
				print('O que vc quer alterar. ')
				print('-digite sair para cancelar a edicao-')
				print('	>		nome')
				print('	>		pais')

				chave = input('Escolha o que vc quer editar escrevendo a palavra como esta escrita acima: ')
				if (chave == 'nome')or(chave == 'pais'):
					alteracao = input('Digite o novo nome: ')
					editar_montadora(bd_montadoras, bd_veiculos, id_montadora, chave, alteracao)
					break

				elif chave == 'sair':break

				else:
					print('Digite uma opcao valida!!!')

			else:
				print( 'Montadora com o id {} nao existe na lista ...'.format(id_montadora) )

		elif opcao == 5:#  - Acrecentar um veiculo a lista 
			limpar()
			print('\n-Acrescentando um novo veiculo-')
			nome_veiculo = input('Digite o nome do veiculo: ')
			ano_veiculo = int( input('Digite o ano do veiculo: ') )
			montadora_veiculo = input('Digite a montadora do veiculo: ')
			if not( verifica_montadora(bd_montadoras, montadora_veiculo) ):
				preco = float( input('Digite a faixa de preco do veiculo: ') )
				motor = float( input('Digite a potencia do motor do veiculo: ') )
				incrementador_de_veiculos(bd_montadoras, montadora_veiculo)
				bd_veiculos.append( acrecentar_veiculo(nome_veiculo, ano_veiculo, montadora_veiculo, preco, motor) )
				print('Veiculo cadastrado com sucesso ...')
			else:
				print('Montadora {} nao cadastrada ainda. Cadastre a montadora primeiro.'.format(montadora_veiculo))
			
		elif opcao == 6:#  - Listar veiculo ja cadastrados 
			while True:
				limpar()
				print('=============Mostrar veiculos===========')
				print('-digite sair para cancelar a edicao-')
				print('1  - listar todos')
				print('2  - listar por montadora')
				print('3  - listar por ano')
				print('4  - listar por faixa de preco')
				print('5  - listar motor e faixa de preco')
				menu = int( input('Digite a opcao desejada: ') )
				if menu == 1:#listar todos
					limpar()
					listar_veiculos(bd_veiculos)
					break

				elif menu == 2:#listar por montadoras
					limpar()
					listar_montadoras(bd_montadoras)
					id_montadora = int( input('Digite o id da montadora para ver seus veiculos: ') )
					try:
						listar_por_montadora(bd_montadoras, bd_veiculos, bd_montadoras[id_montadora]['nome'])
					except Exception:
						print('Digite um id valido!!!')

					break

				elif menu == 3:#listar por ano
					limpar()
					ano = int( input('Digite um ano para a pesquisa: ') )
					listar_por_ano(bd_veiculos, ano)
					print('(caso nao apareca nada e porque nao tem mesmo)')
					break

				elif menu == 4:#por faixa de preco
					limpar()
					preco = float( input('Digite uma faixa de preco para a pesquisa: ') )
					listar_faixa_preco(bd_veiculos, preco)
					print('(caso nao apareca nada e porque nao tem mesmo)')
					break

				elif menu == 5:#preco por motor
					limpar()
					motor = float( input('Digite um motor para a pesquisa:') )
					listar_por_motor(bd_veiculos, motor)
					print('(caso nao apareca nada e porque nao tem mesmo)')
					break

				elif menu == 0:break

				else:
					print('Digite uma opcao valida!!!')

		elif opcao == 7:#  - Apagar veiculo cadastrado 
			limpar()
			print('------removendo-----')
			listar_veiculos(bd_veiculos)
			id_veiculo = int( input('Digite o id do veiculo que deseja excluir da lista: ') )
			if( remover_veiculo(bd_veiculos, bd_montadoras, id_veiculo) ):
				print( 'veiculo {} removido com sucesso!'.format(id_veiculo) )
			else:
				print( 'veiculo {} nao encontrado na lista ...'.format(id_veiculo) )

		elif opcao == 8:#  - Editar veiculo cadastrado 
			limpar()
			listar_veiculos(bd_veiculos)
			id_veiculo = int( input('Digite o id do veiculo que deseja editar: ') )
			while True:
				print('O que vc quer alterar. ')
				print('-digite sair para cancelar a edicao-')
				print('	>		nome')
				print('	>		ano')
				print('	>		montadora')
				print('	>		preco')
				print('	>		motor')
				chave = input('Escolha o que vc quer editar escrevendo a palavra como esta escrita acima: ')

				if (chave == 'nome')or(chave == 'ano')or(chave == 'montadora'):
					if chave == 'montadora':
						while True:
							print('Montadoras disponiveis para troca ...')
							listar_montadoras(bd_montadoras)
							id_montadora = int( input('Escolha a nova montadora digitando a id dela: ') )
							if verifica_montadora(bd_montadoras, id_montadora):
								decrementador_de_veiculos(bd_montadoras, bd_veiculos, bd_veiculos[id_veiculo]['montadora'])
								editar_veiculo(bd_veiculos, id_veiculo, chave, bd_montadoras[id_montadora]['nome'])
								incrementador_de_veiculos(bd_montadoras, bd_veiculos[id_veiculo]['montadora'])
								break
							else:
								print('Digite uma opcao valida!!!')
						break

					elif chave == 'sair':break

					else:
						alteracao = input('Digite a alteracao: ')
						editar_veiculo(bd_veiculos, id_veiculo, chave, alteracao)
						break

				elif (chave == 'preco')or(chave == 'motor'):
					alteracao = float( input('Digite um novo valor: ') )
					editar_veiculo(bd_veiculos, id_veiculo, chave, alteracao)
					break
				else:
					print('Digite uma opcao valida!!!')

		elif opcao == 0:#  - Sair
			salvar_veiculos(bd_veiculos)
			salvar_montadoras(bd_montadoras)
			break
		
		else:
			print('\nDigite uma opção valida!!!\n')

	print('FIM.')

if __name__ == '__main__':
	main()