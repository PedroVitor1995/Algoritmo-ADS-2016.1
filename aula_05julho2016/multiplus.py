def main():
	print 'Q9'
	numero_entrada = input('Digite um numero: ')
	multiplos(numero_entrada, 1)

def multiplos(numero, order):
	if order > 10:
		print 'FIM.'
	else:
		mult = numero*order
		print 'M = %d' % mult
		multiplos(numero, order+1)


if __name__ == '__main__':
	main()