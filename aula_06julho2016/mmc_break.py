#By E.
def main():
	num1, num2 = input('N1: '), input('N2: ')
	resultado = mmc(num1, num2)
	print 'MMC = %d' % resultado

def mmc(numero1, numero2):
	multiplo = 1 

	while True:
		if multiplo % numero1 == 0 and multiplo % numero2 == 0:
			return multiplo
		else:
			multiplo = multiplo + 1


if __name__ == '__main__':
	main()