def main():
	quantidades_fichas = int(input('Quantidade de fichas: '))
	fichas = [0] * quantidades_fichas
	for i in range(quantidades_fichas):
		ficha = [0] * 3
		numero = int(input('Numero de identificacao do boi: '))
		nome  = input('Nome do boi: ')
		peso  = float(input('Peso do boi(em kg): '))
		ficha = [numero,nome,peso]
		fichas[i] = ficha
	menor_peso = fichas[0][2]
	numero_identificacao_menor = fichas[0][0]
	for i in range(1,quantidades_fichas):
		if menor_peso < fichas[i][2]:
			numero_identificacao_menor = numero_identificacao_menor
			menor_peso = menor_peso
		else:
			numero_identificacao_menor = fichas[i][0] 
			menor_peso = fichas[i][2]
		menor_peso = menor_peso
	maior_peso = fichas[0][2]
	numero_identificacao_maior = fichas[0][0]
	for i in range(1,quantidades_fichas):
		if maior_peso > fichas[i][2]:
			numero_identificacao_maior = numero_identificacao_maior
			maior_peso = maior_peso
		else:
			numero_identificacao_maior = fichas[i][0] 
			maior_peso = fichas[i][2]
		maior_peso = maior_peso
	print('O numero de identificacao eh %d e o peso eh %.2f do boi mais magro' \
	% (numero_identificacao_menor,menor_peso))
	print('O numero de identificacao eh %d e o peso eh %.2f do boi mais gordo' \
	% (numero_identificacao_maior,maior_peso))
if __name__ == '__main__':
	main()