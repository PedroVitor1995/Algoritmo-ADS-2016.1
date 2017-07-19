def main():
	fichas = []
	while True:
		ficha = []
		ficha.append(int(input('Numero de identificacao do boi: ')))
		ficha.append(input('Nome do boi: '))
		ficha.append(float(input('Peso do boi(em kg): ')))
		fichas.append(ficha)
		while True:
			resposta = input('Deseja continua "S ou N": ')
			if resposta == 'S' or resposta == 'N':
				break
		if resposta == 'N':
			break
		else:
			continue
	menor_peso = fichas[0][2]
	numero_identificacao_menor = fichas[0][0]
	for i in range(1,len(fichas)):
		if menor_peso < fichas[i][2]:
			numero_identificacao_menor = numero_identificacao_menor
			menor_peso = menor_peso
		else:
			numero_identificacao_menor = fichas[i][0] 
			menor_peso = fichas[i][2]
		menor_peso = menor_peso
	maior_peso = fichas[0][2]
	numero_identificacao_maior = fichas[0][0]
	for i in range(1,len(fichas)):
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