def main():
	quantidade_teste = int(input('Quantidade de teste: '))
	for i in range(quantidade_teste):
		valores = input('Valores do Comeco e Fim da sequencia: ').split(' ')
		comeco = int(valores[0])
		fim = int(valores[1])
		sequencia = ''
		for j in range(comeco,fim+1):
			sequencia += str(j)
		primeira_sequencia = sequencia
		segunda_sequencia = ''
		for numero in sequencia[::-1]:
			segunda_sequencia += numero
		sequencia_espelho = primeira_sequencia + segunda_sequencia
		print(sequencia_espelho)
if __name__ == '__main__':
	main()