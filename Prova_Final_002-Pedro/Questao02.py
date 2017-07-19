def main():
	quantidade_casos = int(input('Quantidade de casos: '))
	for i in range(quantidade_casos):
		valores = input('A quantidade de alunos e um numero secreto: ').split(' ')
		quantidade_alunos = int(valores[0])
		valor_secreto = int(valores[1])
		valores = input('Valores escolhidos: ').split(' ')
		achou_exato = 0
		for j in range(quantidade_alunos):
			if int(valores[j]) == valor_secreto:
				achou_exato = j + 1
		if achou_exato > 0:
			print(achou_exato)
		else:
			diferenca = 0
			achou_proximo = 0
			if valor_secreto > int(valores[0]):
				diferenca = valor_secreto - int(valores[0])
			else:
				diferenca = int(valores[0]) - valor_secreto
			for k in range(quantidade_alunos):
				if valor_secreto > int(valores[k]):
					if diferenca < (valor_secreto - int(valores[k])):
						achou_proximo = k + 1
				else:
					if diferenca < (valor_secreto - int(valores[k])):
						achou_proximo = k + 1
			print(achou_proximo)

if __name__ == '__main__':
	main()