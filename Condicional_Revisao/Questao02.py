#__*__  encoding:utf8 __*__
"""2. Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido."""
def main():
	letra = raw_input('digite uma letra "F ou f" ou "M ou m": ')
	if letra == 'F' or letra == 'f':
		print('Feminino')
	elif letra == 'M' or letra == 'm':
		print('Masculino')
	else:
		print('Sexo invalido')
if __name__ == '__main__':
	main()