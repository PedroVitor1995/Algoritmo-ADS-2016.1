#__*__  encoding:utf8 __*__
"""2. Leia uma frase e mostre cada palavra da frase em uma linha separada."""
def main():
	frase = raw_input('Digite uma frase: ')
	frase = frase.split()
	for i in range(len(frase)):
		print frase[i]
	# espaco = ' '
	# for letra in espaco:
		# frase = frase.replace(letra,'\n')
	# print frase
if __name__ == '__main__':
	main()