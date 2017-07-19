#__*__  encoding:utf8 __*__
"""3. Leia uma frase e gere uma nova frase, retirando os espaços entre as palavras."""
def main():
	frase = raw_input('Digite uma frase: ')
	espaco = ' '
	for letra in espaco:
		nova_frase = frase.replace(letra,'')
	print nova_frase
if __name__ == '__main__':
	main()