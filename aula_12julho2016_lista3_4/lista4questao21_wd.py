def main():
	numero_1, numero_2 = input("primeiro numero: "), input("segundo numero: ")
	resultado = 0

	while numero_2 > 0:
		resultado = resultado + numero_1
		numero_2 = numero_2 - 1

	print "A multiplicacao eh: %d" %resultado

if __name__ == '__main__':
	main()