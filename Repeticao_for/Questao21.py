def main():

	numerador = 1
	denominador = 1

	for i in range(1,50+1):
		print('S = %d / %d ') % (numerador,denominador)
		numerador = numerador + 2
		denominador = denominador + 1

if __name__ == '__main__':
	main()
