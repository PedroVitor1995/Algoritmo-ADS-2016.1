from Questao01_funcoes import *
def main():
	arquivo1 = []
	arquivo2 = []
	arquivo1 += inicializar_partidos()
	arquivo2 += inicializar_candidatos()
	while True:
		menu = ' 1 - Consultar votos validos\
		\n 2 - Consultar quociente eleitoral\
		\n 3 - Consutar total de votos por coligaçao\
		\n 4 - Consultar total de vagas por (quociente partidario)\
		\n 5 - Consultar vargas de sobra\
		\n 0 - Sair\n Opcao: '
		opcao = int(input(menu))
		if opcao == 1:
			votos_validos(arquivo2)
		elif opcao == 2:
			quociente_eleitoral(arquivo2)
		elif opcao == 3:
			votos_por_coligacao(arquivo1,arquivo2)
		elif opcao == 4:
			vagas_quociente_partidario(arquivo1,arquivo2)
		elif opcao == 5:
			vargas_sobra(arquivo1,arquivo2)
		elif opcao == 0:
			break
if __name__ == '__main__':
	main()