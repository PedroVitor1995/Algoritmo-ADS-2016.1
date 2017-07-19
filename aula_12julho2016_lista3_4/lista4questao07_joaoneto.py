def main():
	numero = input("informe um numero:")
	numero_da_lista = input('Numero: ')
	while numero != numero_da_lista:
		numero_da_lista = input('Nada. Continue numero: ')

	print("o numero digitado %d") %(numero)

if __name__ == '__main__':
	main()