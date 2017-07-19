#__*__  encoding:utf8 __*__
"""1. Faça a criptografia de uma frase digitada pelo usuário. Na criptografia, a frase deverá ser invertida e as
consoantes deverão ser substituídas pelo caractere #."""
def main():
	frase = raw_input('Digite uma frase: ')
	consoantes = 'BCDFGHJKLMNPQRSTVXYWZbcdfghjklmnpqrstvxywz'
	for letra in consoantes:
		if letra in frase:
			frase = frase[::-1].replace(letra,'#')
	print frase
if __name__ == '__main__':
	main()