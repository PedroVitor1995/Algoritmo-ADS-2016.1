#__*__  encoding:utf8 __*__
"""38. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o
resultado em forma de fração."""
def main():
	print('Primeira fracao')
	numerador1 = input('Numerador: ')
	denominador1 = input('Denominador: ')
	print('Segunda fracao')
	numerador2 = input('Numerador: ')
	denominador2 = input('Denominador: ')
	numerador = numerador1 + numerador2
	denominador = denominador1 + denominador2

	print ('%d / %d') % (numerador,denominador)

if __name__ == '__main__':
	main()