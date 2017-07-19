#__*__  encoding:utf8 __*__
"""9. Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar outro
valor deve aparecer valor inválido."""
def main():
	numero = input('Digite um numero: ')
	if numero == 1:
		print('Domingo')
	elif numero == 2:
		print('Segunda')
	elif numero == 3:
		print('Terca')
	elif numero == 4:
		print('Quarta')
	elif numero == 5:
		print('Quinta')
	elif numero == 6:
		print('Sexta')
	elif numero == 7:
		print('Sabado')
	else:
		numero = input('Digite um numero valido de 1 a 7:')
		if numero == 1:
			print('Domingo')
		elif numero == 2:
			print('Segunda')
		elif numero == 3:
			print('Terca')
		elif numero == 4:
			print('Quarta')
		elif numero == 5:
			print('Quinta')
		elif numero == 6:
			print('Sexta')
		elif numero == 7:
			print('Sabado')
if __name__ == '__main__':
	main()