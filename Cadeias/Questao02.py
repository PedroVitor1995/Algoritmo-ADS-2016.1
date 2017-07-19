#__*__  encoding:utf8 __*__
"""2. Leia uma frase e mostre cada palavra da frase em uma linha separada."""
def main():
	frase = raw_input('Digite uma frase: ')
	espaco = ' '
	for letra in espaco:
		if letra in frase:
			frase = frase.replace(letra,'\n')
	print frase
if __name__ == '__main__':
	main()