#__*__  encoding:utf8 __*__
"""1. Leia um número e mostre na tela se o número é positivo ou negativo."""
def main():
	numero = input('Digite um numero: ')
	if numero > 0:
		print('numero positivo')
	elif numero < 0:
		print('numero negativo')

if __name__ == '__main__':
	main()