"""25. Em uma eleicao presidencial existem 3 (tres) candidatos. Os votos sao informados atraves de codigos.
Os dados utilizados para a contagem dos votos obedecem a seguinte codificacao:
 1, 2, 3 = voto para os respectivos candidatos;
 9 = voto nulo;
 0 = voto em branco;
Escreva um algoritmo que leia o codigo votado por N eleitores. Ao final, calcule e escreva:
a) total de votos para cada candidato;
b) total de votos nulos;
c) total de votos em branco;
d) quem venceu a eleicao."""
def main():
	quantidade_eleitores = input('Digite a quantidade de eleitores a participar da eleicao: ')

	total_votos_candidato1 = 0
	total_votos_candidato2 = 0
	total_votos_candidato3 = 0
	total_votos_nulos = 0
	total_votos_branco = 0

	print('\nCandidato1 - 1 , Candidato2 - 2, Candidato3 - 3, Voto Nulo - 9, Voto em branco - 0')


	for i in range(1, quantidade_eleitores + 1):

		codigo_votado = input('\nDigite o codigo votado pelo eleitor: ')

		if codigo_votado == 1:
			total_votos_candidato1 += 1
		elif codigo_votado == 2:
			total_votos_candidato2 += 1
		elif codigo_votado == 3:
			total_votos_candidato3 += 1
		elif codigo_votado == 9:
			total_votos_nulos += 1
		elif codigo_votado == 0:
			total_votos_branco += 1


	print('\nA quantidade de votos para o Candidato1 foi %d ') % total_votos_candidato1
	print('\nA quantidade de votos para o Candidato2 foi %d ') % total_votos_candidato2
	print('\nA quantidade de votos para o Candidato3 foi %d ') % total_votos_candidato3
	print('\nA quantidade de votos nulos foi %d ') % total_votos_nulos
	print('\nA quantidade de votos em branco foi %d ') % total_votos_branco

	if total_votos_candidato1 > total_votos_candidato2 and total_votos_candidato1 > total_votos_candidato3:
		print('\nO Candidato1 venceu a eleicao ')
	elif total_votos_candidato2 > total_votos_candidato1 and total_votos_candidato2 > total_votos_candidato3:
		print('\nO Candidato2 venceu a eleicao ')
	elif total_votos_candidato3 > total_votos_candidato1 and total_votos_candidato3 > total_votos_candidato2:
		print('\nO Candidato3 venceu a eleicao ')
if __name__ == '__main__':
	main()