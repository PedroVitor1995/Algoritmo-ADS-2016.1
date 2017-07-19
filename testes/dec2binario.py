def main():
	numero_dec = input('Digite um valor[0-255]')
	numero_bin = 0
	aux = 1
	while numero_dec > 0:
		if numero_dec % 2 != 0:
			numero_bin += aux
		aux *= 10
		numero_dec = numero_dec / 2

	print numero_bin

if __name__ == '__main__':
	main()