"""13. Leia N e uma lista de N numeros e escreva o maior numero da lista."""
def main():
	numero_n = input('Digite o valor de N: ')
	maior = 0

	for i in range(1,numero_n+1):
		lista_numero_n = input('Digite um numero: ')

		if i == 1:
			maior = lista_numero_n
		else:
			if lista_numero_n > maior:
				maior = lista_numero_n
	print maior


if __name__ == '__main__':
	main()