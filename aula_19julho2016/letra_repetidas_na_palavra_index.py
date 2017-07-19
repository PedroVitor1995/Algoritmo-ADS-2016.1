def main():
	palavra = raw_input('Frase: ')

	for i in range(len(palavra)):
		contador = 0
		for j in range(i+1, len(palavra)):
			if palavra[i] == palavra[j]:
				print 'Letra %s Repetida' % palavra[i]
		


if __name__ == '__main__':
	main()