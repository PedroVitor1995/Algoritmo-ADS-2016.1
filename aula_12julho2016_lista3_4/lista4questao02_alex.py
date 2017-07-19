def main():
	multiplo = 1
	numero1 = input('Digite o primeiro numero:')
	numero2 = input('Digite osegundo numero:')
	while True:
		if multiplo % numero1 == 0 and multiplo % numero2 == 0:
			mmc = multiplo
			print mmc
			break
		else: 
			multiplo += 1


if __name__ == '__main__':
	main()