def main():
	numeros = []

	#Receber numeros
	for i in range(10):
		numeros.append(input())

	#Aplicar regra da questao
	for i in range(10):
		if numeros[i] <= 0:
			numeros[i] = 1

	#Escreve resultado
	for i in range(10):
		print "X[%d] = %d" % (i, numeros[i])


if __name__ == '__main__':
	main()