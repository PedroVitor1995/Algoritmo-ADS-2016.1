"""9. Confira o resultado de uma competicao de natacao entre dois clubes. O programa deve ler o numero da
prova e a quantidade de nadadores. O fim dos dados e indicado pelo numero da prova igual a 0 e
quantidade de nadadores igual a 0. A seguir, para cada nadador devera ler nome, classificacao, tempo,
clube (a ou b) e determinar os pontos obtidos por cada clube, de acordo com o seguinte criterio:
Lugar Pontos
1 - 9
2 - 6
3 - 4
4 - 3
Ao final, o algoritmo deve escreva os totais de pontos de cada clube, indicando o clube vencedor"""
def main():

	ponto_1_a = 0
	ponto_2_a = 0
	ponto_3_a = 0
	ponto_4_a = 0
	ponto_1_b = 0
	ponto_2_b = 0
	ponto_3_b = 0
	ponto_4_b = 0
	ponto_clube_a = 0
	ponto_clube_b = 0

	while True:

		numero_prova = input('Digite o numero da prova ou 0 para sair: ')
		quantidade_nadadores = input('Digite a quantidade de nadadores ou 0 para sair: ')


		if numero_prova == 0 and quantidade_nadadores == 0:
			break
		else:
			for i in range(1,quantidade_nadadores+1):
				nome_nadador = raw_input('Digite o nome do nadador: ')
				classificacao_nadador = input('Digite a classificacao do nadador: ')
				tempo = input('Digite o tempo do nadador: ')
				clube = raw_input('\nDigite o clube do nadador "a" ou "b": ')

				if clube == 'a':
					if classificacao_nadador == 1:
						ponto_1_a = ponto_1_a + 9
					elif classificacao_nadador == 2:
						ponto_2_a = ponto_2_a + 6
					elif classificacao_nadador == 3:
						ponto_3_a = ponto_3_a + 4
					elif classificacao_nadador == 4:
						ponto_4_a = ponto_4_a + 3
				elif clube == 'b':
					if classificacao_nadador == 1:
						ponto_1_b = ponto_1_b + 9
					elif classificacao_nadador == 2:
						ponto_2_b = ponto_2_b + 6
					elif classificacao_nadador == 3:
						ponto_3_b = ponto_3_b + 4
					elif classificacao_nadador == 4:
						ponto_4_b = ponto_4_a + 3

	ponto_clube_a = ponto_clube_a + (ponto_1_a + ponto_2_a + ponto_3_a + ponto_4_a)
	ponto_clube_b = ponto_clube_b + (ponto_1_b + ponto_2_b + ponto_3_b + ponto_4_b)

	print('Total de pontos que o clube "a" fez foi %d ') % ponto_clube_a
	print('Total de pontos que o clube "b" fez foi %d ') % ponto_clube_b

	if ponto_clube_a > ponto_clube_b:
		print('O clube vencedor foi o clube "a" ')
	else:
		print('O clube vencedor foi o clube "b" ')




if __name__ == '__main__':
	main()