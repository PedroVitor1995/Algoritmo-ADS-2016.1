from funcoes import *
def main():
	bd_registros = []
	bd_paises = []
	bd_registros += registros_medalhas()
	while True:
		print('-----------Opcoes--------\n')
		print('1 - Adicionar registro de medalha ')
		print('2  - Listar registro de medalha')
		print('3  - Remover registro de medalha')
		print('0  - Sair da aplicacao.')
		opcao = input('Digite a opcao desejada: ')
		if opcao == 1:
			print('-----------Adicionando registro--------\n')
			nome = raw_input('Digite o nome do atleta ou equipe: ')
			esporte = raw_input('Digite o nome do esporte: ')
			modalidade = raw_input('Digite a modalidade (Masculino | Feminino | Misto): ')
			while  True:
				tipo_medalha = raw_input('Digite o tipo de medalha (Ouro |Prata | Bronze): ')
				if tipo_medalha == 'Ouro' or tipo_medalha == 'Prata' or tipo_medalha == 'Bronze':
					break
				else:
					print('A medalha nao eh valida.')
			nome_pais = raw_input('Digite o nome do pais: ')
			bd_registros.append(acrecentar_medalhas(nome, esporte , modalidade , tipo_medalha , nome_pais))
			print('Medalha cadastrada com sucesso ...')
		elif opcao == 2:
			while True:
				print('-----------Opcoes--------\n')
				print('1  - Listar medalha por tipo e pais')
				print('2  - Listar registro de medalha')
				print('3  - Remover registro de medalha')
				print('0  - Voltar para o menu principal')
				opcao = input('Digite a opcao desejada: ')
				if opcao == 1:
					tipo = raw_input('Tipo da medalha (Ouro |Prata | Bronze): ')
					if tipo == 'Ouro' or tipo == 'Prata' or medalha == 'Bronze':
						nome_pais = raw_input('Digite o nome do pais:')
						for pais in range(len(bd_registros)):
							if tipo == bd_registros[pais]['medalha']:
								print('----------------------------\n')
								for medalha in range(len(bd_registros)):
									print('Id:  {}'.format(medalha))
									print('Esporte: {}'.format(esporte))
				elif opcao == 0:
					break				


		elif opcao == 0:
			break



if __name__ == '__main__':
	main()