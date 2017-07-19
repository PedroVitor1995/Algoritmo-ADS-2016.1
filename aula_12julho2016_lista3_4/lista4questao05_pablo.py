def mainha():
	numero_x = input("Digite o numero X: ")
	numero_n = input("Digite o numero N: ")

	while numero_n > 2:
		resultado = numero_x / float(numero_n)
		print resultado
		numero_x = resultado
		numero_n -= 1

if __name__ == '__main__':
	mainha()