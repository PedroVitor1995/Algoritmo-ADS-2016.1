def main():
	print "Divisores..."
	divisores()

def divisores():
	numero = input('Digite um numero:')

	while numero != 0:
		for i in range(numero, 0,-1):
			if numero % i == 0:
				print "%d eh divisor" % (i)

		numero = input('Outro numero ou 0: ')

	print 'FIM.'

if __name__ == '__main__':
	main()