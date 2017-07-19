#__*__  encoding:utf8 __*__
"""1. Faça a criptografia de uma frase digitada pelo usuário. Na criptografia, a frase deverá ser invertida e as
consoantes deverão ser substituídas pelo caractere #."""
def main():
 	frase = raw_input('Digite uma frase: ')
 	consoantes = 'bcdfghlklmnpqrstvywxz'
 	frase = frase.lower()
 	frase_inversa = ''
 	for i in range(len(frase)-1,-1,-1):
 		frase_inversa += frase[i]
 	for letra in consoantes:
 		frase_inversa = frase_inversa.replace(letra, "#")
 	print frase_inversa
if __name__ == '__main__':
	main()