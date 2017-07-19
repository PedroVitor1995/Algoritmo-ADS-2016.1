from Questao06_funcoes import *
def main():
	bd_alunos = []
	bd_alunos += inicializar_alunos()
	while True:
		menu = ' 1 - Listar \n 2 - Buscar \n 0 - Sair \n Opcao: '
		opcao = int(input(menu))
		if opcao == 1:
			while True:
				menu1 = ' 1 - Listar tabela com as notas, media e situacao \n'\
				        ' 2 - Listar tabela com contagem e percentual por situacao \n'\
				        ' 3 - Listar tabela ordenada por nota em ordem decrescente \n'\
				        ' 0 - Sair \n Opcao: '
				resposta = int(input(menu1))
				
				if resposta == 1:
					listar_notas_media_situacao(bd_alunos)
				elif resposta == 2:
					listar_contagem_e_percentual_por_situação(bd_alunos)
				elif resposta == 3:
					menu2 = ' 1 - Listar todos \n 2 - Listar um quantidade desejada \n'\
					        ' 0 - Sair \n Opcao: '
					chave = int(input(menu2))
					if chave == 1:
						listar_tabela_ordenada_por_nota_decrescente_todos(bd_alunos)
					elif chave == 2:
						quantidade_desejadas = int(input('Quantidade que deseja listar: '))
						listar_tabela_ordenada_por_nota_decrescente_quantidade_desejadas(bd_alunos,quantidade_desejadas)
					elif chave == 0:
						break
				elif resposta == 0:
					break
		elif opcao == 2:
			while True:
				menu3 = ' 1 - Buscar alunos por parte do nome\n'\
						' 2 - Buscar alunos por faixa de nota\n'\
						' 3 - Buscar alunos por media considerando apenas os alunos Ativos\n'\
						' 0 - Sair \n Opcao: '
				escolha = int(input(menu3))
				if escolha == 1:
					parte_nome = input('Parte do nome: ')
					buscar_alunos_por_parte_nome(bd_alunos,parte_nome)
				elif escolha == 2:
					faixa_nota = float(input('Faixa de notas:'))
					buscar_alunos_por_faixa_nota(bd_alunos,faixa_nota)
				elif escolha == 3:
					faixa_nota_a = float(input('Faixa de medias: '))
					buscar_alunos_A_por_media_(bd_alunos,faixa_nota_a)
				elif escolha == 0:
					break
		elif opcao == 0:
			salvar_alunos(bd_alunos)
			break
if __name__ == '__main__':
	main()