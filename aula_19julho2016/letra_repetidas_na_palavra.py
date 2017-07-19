def main():
	palavra = raw_input('Frase: ')

	for letra in palavra:
		contador = 0
		for letra2 in palavra:
			if letra == letra2:
				contador += 1
		if contador > 1:
			print 'Letra %s Repetida' % letra
		


if __name__ == '__main__':
	main()