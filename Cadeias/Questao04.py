#__*__  encoding:utf8 __*__
"""4. Leia uma frase e gere uma nova frase, duplicando cada caractere da frase digitada."""
def main():
	frase = raw_input('Digite uma frase: ')
	nova_frase = ''
	for letra in frase:
		nova_frase += frase.replace(frase,letra*2)
	print nova_frase
if __name__ == '__main__':
	main()