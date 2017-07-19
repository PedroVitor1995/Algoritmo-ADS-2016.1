def main():
	teste = input('')
	letra_normal = ''
	letra_ascii = ''
	for i in range(teste):
		string = raw_input('')
		qtd = input('')
		for letra in string:
			letra_ascii = ord(letra) - qtd
			if letra_ascii < 65:
				letra_normal += chr(91 - (65 - letra_ascii))
			else:
				letra_normal += chr(letra_ascii)
		print letra_normal
		letra_normal = ''
		letra_ascii = ''

if __name__ == '__main__':
	main()