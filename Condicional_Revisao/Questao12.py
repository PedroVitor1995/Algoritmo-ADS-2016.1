#__*__  encoding:utf8 __*__
""""""
def main():
	numero = input('Digite um numero: ')
	numero_inteiro = int(numero)
	numero_decimal = float(numero)
	diferenca = numero_decimal - numero_inteiro
	if numero_decimal == numero_inteiro:
		print('Numero inteiro')
	else:
		print('Numero decimal')

if __name__ == '__main__':
	main()