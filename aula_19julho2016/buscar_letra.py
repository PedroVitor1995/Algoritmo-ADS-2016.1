def main():
	palavra = raw_input('Palavra: ')
	letra = raw_input('Letra: ')
	contador = 0

	for l in palavra:
		if letra == l:
			contador += 1
	print 'Qtd = %d' % contador


if __name__ == '__main__':
	main()