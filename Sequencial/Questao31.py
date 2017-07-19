#__*__  encoding:utf8 __*__
"""31. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal."""
def tranforma_decimal(numero_binario):
	if numero_binario >= 1000 and numero_binario <= 1111:
		milhar = numero_binario / 1000
		centena = (numero_binario % 1000) / 100
		dezena = ((numero_binario % 1000) % 100) / 10
		unidade = numero_binario % 10
		numero_decimal = (milhar * 2 ** 3) + (centena * 2 ** 2) + (dezena * 2 ** 1) + (unidade * 2 ** 0)
	elif numero_binario >= 100 and numero_binario <= 111:
		centena = numero_binario / 100
		dezena = (numero_binario % 100) / 10
		unidade = numero_binario % 10
		numero_decimal = (centena * 2 ** 2) + (dezena * 2 ** 1) + (unidade * 2 ** 0)
	elif numero_binario >= 10 and numero_binario <= 11:
		dezena = numero_binario / 10
		unidade = numero_binario % 10
		numero_decimal = (dezena * 2 ** 1) + (unidade * 2 ** 0)
	elif numero_binario >= 0 and numero_binario <= 1:
		unidade = numero_binario % 10
		numero_decimal = unidade * 2 ** 0
	else:
		return'Numero invalido!'
	return numero_decimal

def main():
	numero_binario = raw_input('Digite um numero binario de 4 digitos:')
	numero_decimal = 0
	numero_binario = int(numero_binario)
	numero_decimal = tranforma_decimal(numero_binario)
	print numero_decimal


if __name__ == '__main__':
	main()