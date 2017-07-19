def principal():
	valor = input('Digite um valor[0-10]: ')
	while valor < 0 or valor > 10:
		valor = input('Invalido. Digite outro[0-10]: ')
	print 'Obrigado. Vc digitou: %d' % valor		


if __name__ == '__main__':
	principal()