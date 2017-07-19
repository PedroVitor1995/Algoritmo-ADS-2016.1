def main():
	palavra = raw_input('Palavra: ')
	letra = raw_input('Letra: ')

	for l in palavra:
		if letra == l:
			print 'A letra esta na palavra'
			break


if __name__ == '__main__':
	main()