def main():
	palavra = raw_input('Palavra: ')
	letra = raw_input('Letra: ')

	for i in range(len(palavra)):
		if letra == palavra[i]:
			print 'A letra esta na palavra'
			print 'Posicao %d' % (i+1)
			break


if __name__ == '__main__':
	main()