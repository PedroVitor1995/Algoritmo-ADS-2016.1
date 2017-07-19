def main():
	texto  = input('Digite um texto de ate 20 caracteres: ')
	if len(texto) <= 20:
		quantidade_espaco = 0
		for letra in texto:
			print(quantidade_espaco * ' ' + letra)
			quantidade_espaco += 1
	else:
		print('O texto tem mais de 20 caracteres')
if __name__ == '__main__':
	main()